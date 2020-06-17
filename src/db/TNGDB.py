#!/pkg/python/3.6.8/bin/python3.6
import sqlite3
from socket import gethostname
from pathlib import Path
from .DBItem import DBItem
from .Image import Image

class TNGDB():

	DEFAULT_DBS = {
		'bayonet-09.ics.uci.edu': '/extra/wayne1/preserve/aditeshk'
	}

	def _connect(self, verbose=False):
		if 'sqlpath' not in self.__dict__:
			raise ValueError('self.sqlpath is not defined')
		path = self.sqlpath
		if path.exists() and path.is_file():
			if verbose:
				print('Connecting to existing data base:', path.name)
		elif not path.exists() and path.parent.exists() and path.parent.is_dir():
			if verbose:
				print('Creating new database:', path.name)
		else:
			raise ValueError(f'Invalid database path: {path}')
		return sqlite3.connect(path)

	def _execute(self, method, *args):
		try:
			cursor = self.conn.cursor()
			func = cursor.__getattribute__(method)
			func(*args)
			return cursor.fetchall()
		except Exception as e:
			print(f'Error querying TNG database: {e}')

	def __init__(self, location=None, verbose=False):
		dirname = location
		if not dirname:
			if gethostname() in self.DEFAULT_DBS:
				dirname = self.DEFAULT_DBS[gethostname()]
			else:
				raise ValueError(f'No default database found for {gethostname()}')
		if not isinstance(dirname, Path):
			dirname = Path(dirname)
		self.sqlpath = dirname / 'illustrisTNG.db'
		self.datapath = dirname / 'ILLUSTRIS-TNG'
		self.conn = self._connect(verbose)

	def __getattr__(self, item):
		return  self.conn.cursor().__getattribute__(item)

	def __getitem__(self, key):
		if type(key) is str:
			loc = self.datapath / key
			if not loc.exists():
				return None
			elif loc.is_dir():
				return DBItem(loc)
			else:
				return Image(loc)
		else:
			raise TypeError(f'Could not interpret key of type {type(key)}')
		return 

	def execute(self, *args):
		self._execute('execute', *args)

	def executemany(self, *args):
		self._execute('executemany', *args)

	def executescript(self, *args):
		self._execute('executescript', *args)
	
