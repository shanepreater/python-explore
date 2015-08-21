'''
Created on 21 Aug 2015

@author: shanepreater
'''
from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.testing.config import db
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True)
    name=Column(String(50))
    fullName=Column(String(100))
    password=Column(String(50))
    def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (self.name, self.fullName, self.password)
#End of User

def obtain_session():
    engine = create_engine('sqlite:///tutorial.db')
    engine.echo = True
    
    Session = sessionmaker(bind=engine)
    return Session()

def testSQLAlchemy(session=None):
    '''
        Test the database stuff
    '''
    if(session == None):
        session = obtain_session()
        
    for user in session.query(User).order_by(User.id):
        print(user.id, '=>', "%s(%s)" % (user.fullName, user.name))
        
def loadTestData(session=None):
    print("Loading test data")
    if(session == None):
        session = obtain_session()
        
    session.add_all([
                     User(name="shane",fullName="Shane Preater", password="zagarol"),
                     User(name="nanar", fullName="Hannah Preater", password="floop"),
                     User(name="ben", fullName='Ben Preater', password="tedAndNed"),
                     User(name="gramp", fullName="Steve Preater", password="ruthy"),
                     User(name="nanny ruth", fullName="Ruth Preater", password="chair"),
                     User(name="grampy Pete", fullName="Pete Leycock", password="allotment"),
                     User(name="nanny", fullName="Sue Leycock", password="cruiser"),
                     User(name="leep", fullName="Lee Preater", password="quarry")
                     ])
    session.commit()
def main():
    session = obtain_session()
    print("Testing the database access")
    if session.query(User.id).all():
        print("Test data already loaded")
    else:
        loadTestData(session)  
    return 0

if __name__ == '__main__':
    result = main()
    testSQLAlchemy()
    exit(result)