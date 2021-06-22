# Cyberhive Interview Test

In either Python, C or RUST make a client-server application that every 5s gets a list of running programs on the first server and then sends that information to a second server which saves the sent information to file. Please provide or suggest test coverage for the code you write. The coding test will need to be done in advance of the interview, during which we’ll ask you to screen-share and briefly explain the approach you’ve taken, and how it could be further improved.

# Usage

## Server

`python server/server.py`

## Client

`python client/client.py`

# Improvements

1. Command line arguments for the address and port.
2. Timestamp for data in the output file.
3. File size limit, with data roll-over/wrap-around.

# Tests

* Connection failure
* Multiple connections
* File open failure
* Disk space

