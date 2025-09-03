# Linux File Transfer Guide

> A comprehensive guide for secure file transfer operations between local and remote Linux systems using SSH and SCP protocols.

## Table of Contents

- [Prerequisites](#prerequisites)
- [SSH Connection](#ssh-connection)
- [SCP File Transfer](#scp-file-transfer)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)
- [Security Best Practices](#security-best-practices)

## Prerequisites

Before proceeding with file transfers, ensure you have:

- SSH client installed on your local machine
- Valid SSH credentials for the remote server
- Appropriate file permissions on both local and remote systems
- Network connectivity to the target server

## SSH Connection

### Basic Connection

Connect to your remote server using SSH with custom port:

```bash
ssh sawjal@103.186.20.115 -p 2222
```

### Connection with Additional Options

```bash
# Verbose connection for debugging
ssh -v sawjal@103.186.20.115 -p 2222

# Connection with key-based authentication
ssh -i ~/.ssh/private_key sawjal@103.186.20.115 -p 2222
```

## SCP File Transfer

### Syntax Overview

```bash
scp [OPTIONS] [SOURCE] [DESTINATION]
```

**Basic Pattern:**

```bash
scp -P [PORT] [OPTIONS] [LOCAL_PATH] [USER]@[HOST]:[REMOTE_PATH]
```

### Directory Transfer

Transfer entire directories recursively to remote server:

```bash
# Example: Transfer services directory
scp -P 2222 -r /home/sawjal/sajal/nestorc/nestorc/services sawjal@103.186.20.115:/home/sawjal/projects/nastoc/dev/
```

### File Transfer Examples

#### Single File Transfer

```bash
# Upload single file to remote server
scp -P 2222 /path/to/local/file.txt sawjal@103.186.20.115:/remote/path/

# Download single file from remote server
scp -P 2222 sawjal@103.186.20.115:/remote/path/file.txt /local/destination/
```

#### Multiple Files Transfer

```bash
# Transfer multiple files
scp -P 2222 file1.txt file2.txt file3.txt sawjal@103.186.20.115:/remote/path/

# Transfer files with wildcards
scp -P 2222 *.txt sawjal@103.186.20.115:/remote/path/
```

### Common Options

| Option | Description                         | Example                       |
| ------ | ----------------------------------- | ----------------------------- |
| `-P`   | Specify port number (default: 22)   | `-P 2222`                     |
| `-r`   | Copy directories recursively        | `-r`                          |
| `-v`   | Verbose mode (shows progress)       | `-v`                          |
| `-C`   | Enable compression                  | `-C`                          |
| `-i`   | Specify identity file (private key) | `-i ~/.ssh/id_rsa`            |
| `-o`   | SSH options                         | `-o StrictHostKeyChecking=no` |
| `-l`   | Limit bandwidth (Kbit/s)            | `-l 1000`                     |

## Advanced Usage

### Optimized Transfer Commands

```bash
# High-performance transfer with compression and verbose output
scp -P 2222 -Crv /local/directory/ sawjal@103.186.20.115:/remote/path/

# Transfer with bandwidth limitation
scp -P 2222 -l 1000 largefile.zip sawjal@103.186.20.115:/remote/path/

# Preserve file attributes (timestamps, permissions)
scp -P 2222 -p important_file.txt sawjal@103.186.20.115:/remote/path/
```

### Alternative Transfer Methods

#### Using rsync (recommended for large transfers)

```bash
# Sync directories with progress and resume capability
rsync -avz -e "ssh -p 2222" /local/directory/ sawjal@103.186.20.115:/remote/path/

# Dry run to preview changes
rsync -avz --dry-run -e "ssh -p 2222" /local/directory/ sawjal@103.186.20.115:/remote/path/
```

#### Using tar with SSH for faster directory transfers

```bash
# Compress and transfer in one step
tar czf - /local/directory | ssh -p 2222 sawjal@103.186.20.115 "cd /remote/path && tar xzf -"
```

## Troubleshooting

### Common Issues and Solutions

#### Permission Denied

```bash
# Check file permissions
ls -la /path/to/file

# Fix permissions if needed
chmod 644 file.txt  # For files
chmod 755 directory/  # For directories
```

#### Connection Timeout

```bash
# Test connectivity
ping 103.186.20.115

# Test SSH connection
ssh -v -p 2222 sawjal@103.186.20.115
```

#### Large File Transfer Optimization

```bash
# Use compression for large files
scp -P 2222 -C largefile.zip sawjal@103.186.20.115:/remote/path/

# For very large transfers, consider rsync
rsync -avz --progress -e "ssh -p 2222" largefile.zip sawjal@103.186.20.115:/remote/path/
```

## Security Best Practices

### SSH Key Authentication

1. **Generate SSH key pair:**

   ```bash
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
   ```

2. **Copy public key to remote server:**

   ```bash
   ssh-copy-id -p 2222 sawjal@103.186.20.115
   ```

3. **Use key-based authentication:**
   ```bash
   scp -P 2222 -i ~/.ssh/id_rsa file.txt sawjal@103.186.20.115:/remote/path/
   ```

### Security Recommendations

- ✅ Use SSH keys instead of passwords
- ✅ Verify host fingerprints on first connection
- ✅ Use non-standard SSH ports when possible
- ✅ Regularly update SSH client and server
- ✅ Monitor transfer logs for suspicious activity
- ❌ Avoid transferring sensitive data over untrusted networks
- ❌ Don't use weak passwords or shared accounts

---

**Note:** Replace the example IP address, usernames, and paths with your actual server details. Always test file transfers with small files first before transferring large amounts of data.
