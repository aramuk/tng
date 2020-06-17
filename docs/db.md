# `tng.db`

The submodule facilitates interactions with the database of retrieved information.

## Class `tng.db.TNGDB`

A class for interacting with retrieved TNG data.

### **Methods:**

### `__init__(self, location=None, verbose=False)`

Constructor. Connects to the database.

**Parameters:**
- **location**: the directory containing the SQL database and retrieved image files. Optional on bayonet-09
- **verbose**: display output when connecting to database?

### `execute(self, *args)`

Execute query with error handling. See [`sqlite3.Cursor.execute`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.execute). 

**Parameters:**
- **args**: A single SQL query, followed by any number of parameterized values.

**Returns:** rows found in the query

### `executemany(self, *args)`

Execute query multiple times with error handling. See [`sqlite3.Cursor.executemany`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany). 

**Parameters:**
- **args**: A single SQL query, followed by a sequence of parameterized values.

**Returns:** rows found in the query

### `executemany(self, *args)`

Execute query multiple times with error handling. See [`sqlite3.Cursor.execute`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor.executemany). 

**Parameters:**
- **args**: A single SQL query, followed by a sequence of parameterized values.

**Returns:** rows found in the query

### **Additional Functionality**

This class supports all of the methods of [`sqlite3.Cursor`](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor).

This class supports indexing by `object_id`. Indexing returns an object of type `tng.db.DBItem`.

## Class `tng.db.DBItem`

A class for listing all images associated with a TNG subhalo.

### `__init__(self, path)`

Constructor.

**Parameters:**
- **path**: the path to the subhalo object

### `__iter__(self)`

Lists all images (fits/png; raw/ready) associated with a subhalo.

**Returns:** A generator function

### `raw(self, filetype=None)`

Lists all unprocessed images with the desired filetype

**Parameters:**
- **filetype**: None, 'fits', or 'png'; the type of images to list; 'None' lists both types

**Returns:** A generator function

### `ready(self, filetype=None)`

Lists all processed images with the desired filetype

**Parameters:**
- **filetype**: None, 'fits', or 'png'; the type of images to list; 'None' lists both types

**Returns:** A generator function

### `fits(self, state=None)`

Lists all .fits images with the desired processing state.

**Parameters:**
- **state**: None, 'raw', or 'ready'; the processing state of the images to list; 'None' lists both types

**Returns:** A generator function

### `png(self, state=None)`

Lists all .png images with the desired processing state.

**Parameters:**
- **state**: None, 'raw', or 'ready'; the processing state of the images to list; 'None' lists both types

**Returns:** A generator function

## Class `tng.db.Image`

A class for reading and visualizing images in the database. Only supports 'png' and 'fits' files.

### `__init__(self, path)`

Constructor. Only supports 'png' and 'fits' files.

**Parameters:**
- **path**: the path to the image

### `get_data(self)`

Reads the data from the image file into a matrix.

**Returns:** a `numpy.ndarray` representing the image

### `show(self)`

Visualizes the image as a `matplotlib.pyplot.figure`. Displays colorbands independently for FITS
