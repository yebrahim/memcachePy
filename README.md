# pyMemcache
Simple transactional memory cache written in Python
This implementation is to explore the idea of simple transactional operations on a memory cache. It supports string keys and integer values, but it can easily be generalized for other types as well.

##Supported Operations:

`set(k, v)`: Inserts the given key-value pair into the cache, or updates the value if it already exists.

`get(k)`: Returns the value associated with the given key. Returns None if the key does not exist.

`delete(k)`: Deletes the given key and its value from the cache. Does nothing if the key doesn't exist.

`count(v)`: Returns a count of keys that have the given value. Returns 0 if no such keys exist.

`begin()`: Starts a transaction. Transactions can be nested by calling `begin()` before ending the current transaction.

`rollback()`: Rolls back the current transaction. If this is a nested transaction, only the deepest level transaction is rolled back. Raises a `NO TRANSACTION` exception if no transaction is currently in progress.

`commit()`: Commits all currently open transactions. Raises a `NO TRANSACTION` exception if no transaction is currently in progress.
