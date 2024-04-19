# Red Hat AMQ clients 2023.Q4

This is the first release of AMQ clients as a quarterly release. A quarterly release contains any new minor or major versions 
of a client that are available. Each minor or major release will receive support for 1 year and 6 months and will receive 
CVE fixes or Critical bug fixes. Please refer to the [Detailed Product Life Cycle Policy](https://access.redhat.com/articles/7052871). 

The AMQ C++ AMQ Python were not released in this first release. These will be released in a future quarterly release and
are still supported. Please refer to [Previous Clients Releases](https://access.redhat.com/articles/5043041) for these clients. 

AMQ clients are supported for use on the following operating systems, architectures and platforms. Note: Clients are 
backward compatible.

[Previous Clients Releases](https://access.redhat.com/articles/5043041)

Not all clients are supported on all operating systems. Specific client support is documented in the section titled Specific supported clients and OSs.

## Supported Operating Systems

| Operating system                         | Architecture |
|------------------------------------------|--------------|
| RHEL 9                                   | X86_64       |
| RHEL 8                                   | x86_64       |
| Microsoft Windows Server 2019            | x86_64       |                                              
| Microsoft Windows Server 2016            | x86_64       |
| Microsoft Windows 10 and 11 Professional | x86_64       |                                            

## Supported Platforms

| Client                                     | Platform                                                    | Comments                               |
|--------------------------------------------|-------------------------------------------------------------|----------------------------------------|
| Apache Qpid JMS                            | OpenJDK 11 & 17, Oracle JDK 11 & 17, IBM Semeru JDK 11 & 17 | Windows is tested with Oracle JDK only |
| Red Hat build of AMQP 1.0 JMS Spring Boot  | OpenJDK 11 & 17, Oracle JDK 11 & 17, IBM Semeru JDK 11 & 17 | Windows is tested with Oracle JDK only |
| Red Hat build of Apache Qpid ProtonJ2      | OpenJDK 11 & 17, Oracle JDK 11 & 17, IBM Semeru JDK 11 & 17 | Windows is tested with Oracle JDK only |                                              
| Red Hat build of Apache Qpid Proton DotNet | NET 6.0                                                     |                                        |                                           
| Red Hat build of Rhea                      | Node.js 18                                                  |                                        |

Note: Earlier versions of the JDK are not supported.

## Standards and network protocols

The following standards and protocols are supported where applicable for each client. 

- Version 2.0 of the [Java Message Service API](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Fjcp.org%2Fen%2Fjsr%2Fdetail%3Fid%3D343)
- Version 1.0 of the [Advanced Message Queueing Protocol (AMQP)](https://access.redhat.com/bounce/?externalURL=http%3A%2F%2Fwww.amqp.org%2F)
- Version 1.0 of the AMQP JMS Mapping
- Modern [TCP](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc793) with [IPv6](https://access.redhat.com/bounce/?externalURL=https%3A%2F%2Ftools.ietf.org%2Fhtml%2Frfc2460)
