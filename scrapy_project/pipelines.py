from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import requests

# SQLAlchemy setup
Base = declarative_base()

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String)
    image = Column(String)
    name = Column(String)
    price = Column(String)

class PostgresPipeline:
    def open_spider(self, spider):
        # PostgreSQL connection via SQLAlchemy
        self.engine = create_engine('postgresql://user:password@postgres/scrapydb')
        Base.metadata.create_all(self.engine)  # Automatically create the table
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

        # Ensure the images directory exists
        if not os.path.exists('images'):
            os.makedirs('images')

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()

    def process_item(self, item, spider):
        # Download the image
        img_url = item['Image']
        img_name = os.path.basename(img_url)
        img_path = os.path.join('images', img_name)
        
        # Save image locally
        with open(img_path, 'wb') as f:
            img_data = requests.get(img_url).content
            f.write(img_data)

        # Save to PostgreSQL
        product = Product(
            url=item['Url'],
            image=img_name,  # Store image name
            name=item['Name'],
            price=item['Price']
        )
        self.session.add(product)
        return item
