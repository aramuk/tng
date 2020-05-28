#!/usr/bin/python3

import sqlite3
import socket
from pathlib import Path

class TNGDB():

	DEFAULT_DBS = {
		'bayonet-09.ics.uci.edu': '/extra/wayne1/preserve/aditeshk'
	}

	def _connect(self):
		if 'sqlpath' not in self.__dict__:
			raise ValueError('self.sqlpath is not defined')
		path = self.sqlpath
		if path.exists() and path.is_file():
			print('Connecting to existing data base:', path.name)
		elif not path.exists() and path.parent.exists() and path.parent.is_dir():
			print('Creating new database:', path.name)
		else:
			raise ValueError(f'Invalid database path: {path}')
		return sqlite3.connect(path)


	def __init__(self, location=None):
		dirname = location
		if not dirname:
			if socket.gethostname() in self.DEFAULT_DBS:
				dirname = self.DEFAULT_DBS[socket.gethostname()]
			else:
				raise ValueError('No default database found for {socket.gethostname()}')
		if not isinstance(dirname, Path):
			dirname = Path(dirname)
		self.sqlpath = dirname / 'illustrisTNG.db'
		self.imgpath = dirname / 'ILLUSTRIS-TNG'
		self.conn = self._connect()

	def execute(self, *args):
		try:
			cursor = self.conn.cursor()
			return cursor.execute(*args)
		except Exception as e:
			print(f'Error querying TNG database: {e}')
	
