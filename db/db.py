# -*- coding:utf-8 -*-
# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class Shell(Base):
    '''CREATE TABLE "sitetable" (
    "ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "type_id"  INTEGER NOT NULL,
    "siteurl"  TEXT NOT NULL,
    "sitepass"  TEXT,
    "link"  INTEGER NOT NULL,
    "ip"  TEXT,
    "config"  TEXT NOT NULL,
    "coding"  TEXT NOT NULL,
    "script"  TEXT,
    "submit"  TEXT,
    "remarks"  TEXT,
    "createtime"  TEXT,
    "updatetime"  TEXT,
    "os"  TEXT,
    CONSTRAINT "rul" UNIQUE ("siteurl" ASC, "sitepass" ASC)
    );
    '''
    # 表的名字:
    __tablename__ = 'sitetable'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    type_id = Column(String(20))
    siteurl = Column(String(200))
    sitepass  = Column(String(200))
    link  = Column(String(200))
    ip  = Column(String(200))
    config  = Column(String(200))
    coding  = Column(String(200))
    script  = Column(String(200))
    submit  = Column(String(200))
    remarks  = Column(String(200))
    createtime  = Column(String(200))
    updatetime  = Column(String(200))
    os = Column(String(200))

class ShellType(Base):
    '''table name
    CREATE TABLE "type" (
        "ID"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        "name"  TEXT NOT NULL,
        "ico_path"  TEXT,
        "createtime"  TEXT NOT NULL
        );
    '''
    __tablename__ = 'type'

    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    ico_path = Column(String(20))
    createtime = Column(String(20))

# 初始化数据库连接:
engine = create_engine('sqlite:///shell.db',echo = True)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

