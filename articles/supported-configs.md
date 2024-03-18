# Red Hat AMQ clients 2023.Q1

This is the first release of AMQ clients as a quarterly release. A quarterly release contains any new minor or major versions 
of a client that are available. Each minor or major release will receive support for 1 year and 6 months and will receive 
CVE fixes or Critical bug fixes. Please refer to the [Detailed Product Life Cycle Policy](https://access.redhat.com/articles/7052871). 

The AMQ C++ AMQ Python were not released in this first release. These will be released in a future quarterly release and
are still supported. Please refer to [Previous Clients Releases](https://access.redhat.com/articles/5043041) for these clients. 

AMQ clients are supported for use on the following operating systems, architectures, and JVM versions. Note: Clients are 
backward compatible.

[Previous Clients Releases](https://access.redhat.com/articles/5043041)

Not all clients are supported on all operating systems. Specific client support is documented in the section titled Specific supported clients and OSs.

| Operating system                         | Architecture | JVM                                          |
|------------------------------------------|--------------|----------------------------------------------|
| RHEL 9                                   | X86_64       | OpenJDK 11 &17, Oracle JDK 11, IBM JDK 11    |
| RHEL 8                                   | x86_64       | OpenJDK 11 &17, Oracle JDK 11, or IBM JDK 11 |
| Microsoft Windows Server 2019            | x86_64       | Oracle JDK 11                                |                                              
| Microsoft Windows Server 2016            | x86_64       | Oracle JDK 11                                |
| Microsoft Windows 10 and 11 Professional | x86_64       | Oracle JDK 11                                |                                              

Note: Earlier versions of the JDK are not supported.

## Specific supported clients and OS's

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system	                 | Red Hat build of Apache Qpid JMS	 | Red Hat build of AMQP 1.0 JMS Spring Boot | Red Hat build of Apache Qpid ProtonJ2 | Red Hat build of Apache Qpid Proton DotNet | Red Hat build of Rhea |
|-----------------------------------|-----------------------------------|-------------------------------------------|---------------------------------------|--------------------------------------------|-----------------------|
| RHEL 9 x86_64                     | Yes                               | Yes                                       | Yes                                   | Yes                                        | Yes                   |
| RHEL 8 x86_64                     | Yes                               | Yes                                       | Yes                                   | Yes                                        | Yes                   |
| Microsoft Windows Server 2019     | Yes                               | Yes                                       | Yes                                   | Yes                                        | Yes                   |
| Microsoft Windows Server 2016     | Yes                               | Yes                                       | Yes                                   | Yes                                        | Yes                   |
| Microsoft Windows 11 Professional | Yes                               | Yes                                       | Yes                                   | Yes                                        | Yes                   |
| Microsoft Windows 10 Professional | Yes                               | Yes                                       | Yes                                   | Yes                                        | Yes                   |



## The Red Hat build of Apache Qpid JMS client is supported on the following OSs and JVMs.

Qpid JMS has 2 streams of releases, the 1.X stream which uses the Javax API's and 2.x which uses the Jakarta API's.

| Operating system              | JVM                                             |
|-------------------------------|-------------------------------------------------|
| RHEL 9                        | OpenJDK 11 & 17, Oracle JDK 11, OpenJ 9 11 & 17 |
| RHEL 8                        | OpenJDK 11 & 17, Oracle JDK 11, OpenJ 9 11 & 17 |
| Microsoft Windows Server 2019 | Oracle JDK 11                                   |
| Microsoft Windows Server 2016 | Oracle JDK 11                                   |

Notes:
+ Earlier versions of the JDK are not supported.

### Standards and network protocols

- Version 2.0 of the [Java Message Service API](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fjcp.org%2Fen%2Fjsr%2Fdetail%3Fid%3D343)
- Version 1.0 of the [Advanced Message Queueing Protocol (AMQP)](https://access.redhat.com/bounce/?externalURL=http%3A%2F%2Fwww.amqp.org%2F)
- Version 1.0 of the AMQP JMS Mapping
- Modern [TCP](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc793) with [IPv6](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc2460)


## Red Hat build of AMQP 1.0 JMS Spring Boot is supported on the following OSs and JVMs.

The Spring Boot client has 2 streams of release, the 2.X stream which uses the Javax API's and 3.x which uses the Jakarta API's.

| Operating system              | JVM                                             |
|-------------------------------|-------------------------------------------------|
| RHEL 9                        | OpenJDK 11 & 17, Oracle JDK 11, OpenJ 9 11 & 17 |
| RHEL 8                        | OpenJDK 11 & 17, Oracle JDK 11, OpenJ 9 11 & 17 |
| Microsoft Windows Server 2019 | Oracle JDK 11                                   |
| Microsoft Windows Server 2016 | Oracle JDK 11                                   |

Notes:
+ Earlier versions of the JDK are not supported.

### Standards and network protocols

- Version 2.0 of the [Java Message Service API](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fjcp.org%2Fen%2Fjsr%2Fdetail%3Fid%3D343)
- Version 1.0 of the [Advanced Message Queueing Protocol (AMQP)](https://access.redhat.com/bounce/?externalURL=http%3A%2F%2Fwww.amqp.org%2F)
- Version 1.0 of the AMQP JMS Mapping
- Modern [TCP](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc793) with [IPv6](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc2460)


## Red Hat build of Apache Qpid ProtonJ2 is supported on the following OSs and JVMs.

| Operating system              | JVM                                             |
|-------------------------------|-------------------------------------------------|
| RHEL 9                        | OpenJDK 11 & 17, Oracle JDK 11, OpenJ 9 11 & 17 |
| RHEL 8                        | OpenJDK 11 & 17, Oracle JDK 11, OpenJ 9 11 & 17 |
| Microsoft Windows Server 2019 | Oracle JDK 11                                   |
| Microsoft Windows Server 2016 | Oracle JDK 11                                   |

Notes:
+ Earlier versions of the JDK are not supported.

### Standards and network protocols

- Version 1.0 of the [Advanced Message Queueing Protocol (AMQP)](https://access.redhat.com/bounce/?externalURL=http%3A%2F%2Fwww.amqp.org%2F)
- Version 1.0 of the AMQP JMS Mapping
- Modern [TCP](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc793) with [IPv6](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc2460)


## Red Hat build of Apache Qpid Proton DotNet is supported on the following OSs and JVMs.

| Operating system              | .NET version                        |
|-------------------------------|-------------------------------------|
| RHEL 9                        | .NET Core 3.9                       |
| RHEL 8                        | .NET Core 3.9                       |
| Microsoft Windows Server 2019 | .NET Core 3.9 and .NET Platform x.y |
| Microsoft Windows Server 2016 | .NET Core 3.9 and .NET Platform x.y |


### Standards and network protocols

- Version 1.0 of the [Advanced Message Queueing Protocol (AMQP)](https://access.redhat.com/bounce/?externalURL=http%3A%2F%2Fwww.amqp.org%2F)
- Version 1.0 of the AMQP JMS Mapping
- Modern [TCP](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc793) with [IPv6](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc2460)


## Red Hat build of Rhea is supported on the following OSs and JVMs.

| Operating system              | JavaScript Runtime |
|-------------------------------|--------------------|
| RHEL 9                        | Node.js 18         |
| RHEL 8                        | Node.js 18         |
| Microsoft Windows Server 2019 | Node.js 18         |
| Microsoft Windows Server 2016 | Node.js 18         |
| Microsoft Windows 11          | Node.js 18         |
| Microsoft Windows 10          | Node.js 18         |


### Standards and network protocols

- Version 1.0 of the [Advanced Message Queueing Protocol (AMQP)](https://access.redhat.com/bounce/?externalURL=http%3A%2F%2Fwww.amqp.org%2F)
- Version 1.0 of the AMQP JMS Mapping
- Modern [TCP](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc793) with [IPv6](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc2460)



