## Linux File Transfer Documentation
#### SSH Connection
To connect to the remote server via SSH:
```
ssh sawjal@103.186.20.115 -p 2222
```

## File Transfer with SCP
#### Basic Syntax

```
scp -P [PORT] -r [LOCAL_PATH] [USER]@[HOST]:[REMOTE_PATH]
```

#### Example: Transfer Directory
To recursively copy the entire services directory to the remote server:
```
scp -P 2222 -r /home/sawjal/sajal/nestorc/nestorc/services sawjal@103.186.20.115:/home/sawjal/projects/nastoc/dev/
```


### Common Options
-P: Specify port number (default is 22)

-r: Copy directories recursively

-v: Verbose mode (shows progress)

-C: Enable compression


#### Additional Examples
Transfer Single File

```bash
scp -P 2222 /path/to/local/file.txt sawjal@103.186.20.115:/remote/path/
```
