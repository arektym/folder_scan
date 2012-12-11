from sqlalchemy import  Column, Integer, Unicode, ForeignKey, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
 
Base = declarative_base()
class File(Base):
    __tablename__ = 'file'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode)
    path = Column(Unicode)
    size = Column(Unicode)
    perms = Column(Unicode)
    time_created = Column(Unicode)
    time_modified = Column(Unicode)
    
    def get_filesystem_path(self):
        '''path to image'''
        return self.path + self.name
 
from sqlalchemy.pool import StaticPool
engine = create_engine('sqlite:///files.db', connect_args={'check_same_thread':False}, poolclass=StaticPool)
Base.metadata.create_all(engine)
data = sessionmaker(bind=engine)()

def return_file_atrrs(file_name):
    try: file_ = data.query(Files).filter_by('name')[0]
    except: file_ = None
    if file_:
        print file_.name, file_.size, file_.perms, file_.time_created, file_.time_modified
    else:
        print '%s not found' % file_name

def get_file_list():
    return data.query(File)

def get_file(filename):
    query = data.query(File).filter_by(name=filename)
    if query.all(): return query[0]
    else: return False

def save_in_db(name, path, size, perms, time_c, time_m):
    if not file_exist(name, path):
       file_=File(name=name, size=size, perms=perms, time_created=time_c, time_modified=time_m)
       data.add(file_)
       data.commit()
   
def file_exist(file_name, path):
    resoult = data.query(File).filter_by(name=file_name)
    for file_ in resoult:
        if file_.path == path:
            print 'file already in db'
            return True
    return False
