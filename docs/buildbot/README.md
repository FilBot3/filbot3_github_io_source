# BuildBot

## Overview

`buildbot` is a wonderful CI/CD Framework that can be customized and built upon
to make a CI/CD Platform that uses Docker, Virtual Compute Instances, or local
workers. Here I'll attempt to provide some information I have learned while
using BuildBot to help others make their journeys a lot more smooth. However, I will not go into great detail about how to setup and isntall things like Python, or Docker. Those are things that people will need to figure out on their own. I'll mention the tools I'm using, but setups are outside of the scope of this, I believe.

## Requirements

* Docker with Experimental Features enabled
* Python 3.7

## The Deets

### Docker and the Master

I used Docker to drive most of my BuildBot setup and also to perform builds for my users. That way I was able to provide consistent builds and if one person made changes to the environment, they didn't mess it up for everyone. So this required the BuildBot Master to be a Docker Host. In my setup, I could only get one node so the Docker Host will also be where the build are performed. We'll work a bit of magic to make this happen in the BuildBot Master Configurations.

### Docker and the Workers

My workers were also ran in Docker. I chose to use a different base Docker Image for my worker images so that way my users were more comfortable with that environment for running shell scripts. I found that the Alpine Linux Image that BuildBot provided didn't have Bash and a large portion of my user base expected that to be available. So I made a base Image with my CentOS 7 and set up all the requisite libraries that were needed, and also setup the BuildBot service and its ENTRYPOINT with CMD to be used. Everything else was the same from the Dockerfiles that BuildBot provided except the base Image. Making a base Image for my custom BuildBot Worker allowed me to minimize the changes to certain containers if the base layer was the same. I provided three worker images for my users. One was a ChefDK, one a RBENV and one a RVM image with a common shell script between them that would execute defined tasks regardless of which environment they ran their jobs in. Sure, I could have put the ChefDK with the other two Ruby managers but I've had wonkyness before, so I didn't bother.

### Docker and Docker features

I also setup a Docker Volume with my Chef-Server Admin User configurations using the Chef/Knife 13.7 and newer feature of Knife Profiles. This cut down on the amount of crud I had to have in the Docker Volume and also made it easier to keep a single file and encrypt it rather than a bunch of files in either a single YAML with Ansible or JSON for Chef Data Bags.

I attempted to use Docker Networking, but in an air-gapped, STIG'ed environment, IPv4 is disabled. Sure you could get an exception to have it turned back on, but instead what I did is made the Docker Containers attach to the Docker Host Network and the services only listen on localhost and let my HTTPD/Nginx process handle the SSL/TLS and reverse proxying. This went for the DB, HashiCorp Vault, and BuildBot Master.

### BuildBot Database in Docker

Two more items before moving on to the Configuration for the BuildBot Master. BuildBot uses a SQLite DB by default to store its history and job sync. I chose to move that database to an external database by using a PostgreSQL Docker Container. This allowed me to use a remote database in a sense, and allow for future moves if the database had to be on its own host. I used Ansible and some clever SQL Statements ran at command-line via Ansible to set up the PostgreSQL Database.

### BuildBot Secrets in Docker

For secrets storage I chose to use HashiCorp Vault. This also ran in a container and wrote its secrets to the PostgreSQL database. I figured this then would allow for the Containers and the Storage to be able to be moved whereever they needed to be while still providing the necessary functionality to the BuildBot Master. I use an Ansible Role, sort of Python Module to perform the setup, unsealing and writing of the Vault secrets to be used with BuildBot.

### BuildBot Master Configuration

Finally the BuildBot Master Configuration. In my environment that I controlled in my employer was multiple environments with slightly different yet slightly similar configurations. So I decided that maintaining a single repository with multiple configurations what more desirable. Since the `master.cfg` that BuildBot reads is really just Python, this allowed me to use Python factilities and methods to extend the master.cfg. I was able to create folders with the environment specific configurations and make them loadable to the BuildBot Master dependent upon an environment variable passed to the Master Container at run. The `master.cfg` contained the code and configuration that was common across all nodes such as default ad-hoc jobs, or workers that were available, or web interface configurations. Then I also extended or appended the configurations from the other included Python Modules. Then the rest is passing environment variables to the BuildBot Master Docker Container and then in turn pass those on to the `master.cfg` and its subsequent configurations that were loaded.

### Goodies!

This rough overview allowed me to setup a CI/CD platform that provided a already proven working environment to my customers while also allowing them to bring their own containers if they desired a different work flow. Some extra bonus material was that I invluded a Ruby Gem that I had made that allowed them to use the BuildBot environment similar to that of a Jenkinsfile where they could define a "pipeline" and load up a single thread/process and perform tasks a lot quicker. This was mostly centered around managing a Chef-Server and its Chef-Repository components though. However, writing Ruby code to handle other things isn't too far out of the question. That's a different blog post.



## References

* [BuildBot Homepage](https://buildbot.net)
