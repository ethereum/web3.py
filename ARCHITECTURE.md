methods/*
    These files define all methods callable under
    web3.db.*
    web3.eth.*
    web3.net.*
    web3.personal.*
    web3.shh.*

    Methods and properties are first defined as a dictionary
    and then are converted to real functions and attached to the
    respective objects. This will make it easier to mirror the
    next migrations of the web3.js library. Both types are defined
    in method.py and property.py respectively.

RequestManager
    Is supplied with one Provider at initialisation which
    can be replaced by calling setProvider(). It uses Jsonrpc
    to convert the methods into raw payloads and to validate
    responses attained with receive().
    
    Has three other methods:
    
    - send(data, timeout=None)
        If timeout is None, send blocks until the result is
        available, which it then returns.
        
        If the timeout is 0, send returns immediately, only
        returning the id of the request, which can be used
        to poll with receive() later.

        If the timeout is greater than 0, it blocks until
        either the result is available or the timeout is
        reached, at which point a ValueError is thrown.
        
        send() makes use of the other two functions:

    - forward(data)
        Forwards the data to the provider and returns the
        request id.
    
    - receive(requestid, timeout=0)
        Implements the timeout functionality described in send.
        If timeout is 0, it returns None if the response was
        not available.

Provider
    On initialisation, is started in a separate thread.
    Continuously fetches incoming requests from a queue
    and appends the responses to another queue. Providers
    only receives and returns "raw" requests, JSON validation
    and decoding happens in the Request Manager.
    
    As of now there are two implementations:
        - RPCProvider
        - IPCProvider
