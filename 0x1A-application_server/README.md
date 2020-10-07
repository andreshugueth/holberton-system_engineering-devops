# 0x1A. Application server

<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/9/c7d1ed0a2e10d1b4e9b3.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201007%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201007T155425Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=37d5555e0e3d26d380805088219e2d90dca3e5d3edd6f6a6823ca6125898038d">

## Background Context

Your web infrastructure is already serving web pages via Nginx that you installed in your first web stack project. While a web server can also serve dynamic content, this task is usually given to an application server. In this project you will add this piece to your infrastructure, plug it to your Nginx and make is serve your Airbnb clone project.

## Requirements

### General

* A README.md file, at the root of the folder of the project, is mandatory
* Everything Python-related must be done using python3
* All config files must have comments

### Bash Scripts
* All your files will be interpreted on Ubuntu 16.04 LTS
* All your files should end with a new line
* All your Bash script files must be executable
* Your Bash script must pass Shellcheck (version 0.3.7-5~ubuntu16.04.1 via apt-get) without any error
* The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
* The second line of all your Bash scripts should be a comment explaining what is the script doing
