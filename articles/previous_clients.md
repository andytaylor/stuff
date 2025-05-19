##  Red Hat AMQ clients 2.11 {#clients}

AMQ clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

[Previous Clients Releases](https://access.redhat.com/articles/5043041)

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                            |
| --------------------------------- | :----------------------: | ---------------------------------------------- |
| RHEL 8                            | X86_64                   | OpenJDK 11 &17, Oracle JDK 11, IBM JDK 11 |
| RHEL 7                            | x86_64                   | OpenJDK 11 &17, Oracle JDK 11, or IBM JDK 11          |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 11                                      |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 11                                   |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 11                                   |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 11                                  |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 11                                   |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | :---------------------: | :---------------------: | :-----------------------------------: | :---------------------------: | :----------------------: | :------: |
| RHEL 8 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | Yes      |
| RHEL 7 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | Yes      |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | Yes                            | Yes                      | No       |
| Microsoft Windows Server 2016     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | Yes                            | Yes                      | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                            |
| -------------------------------- | ------------------------------ |
| RHEL 8                           | OpenJDK 11 &17, Oracle JDK 11, IBM JDK 11 |
| RHEL 7                           | OpenJDK 11 &17 or Oracle JDK 11, IBM JDK 11      |
| Microsoft Windows Server 2012 R2 | Oracle JDK 11                   |
| IBM AIX 7.1                      | IBM JDK 11                      |
| Solaris 10 and 11                | Oracle JDK 8                   |

Notes:
+ Earlier versions of the JDK are not supported.
+ The AMQ JMS Client supports the use of the AMQ Pool library.
####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 8                            | GNU C++                      | Compiling as C++11          |
| RHEL 7                            | GNU C++                      | Compiling as C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++11 |
| Microsfot Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                   |
| --------------------------------- | ------------------------------------ |
| RHEL 8                            | Node.js 14                           |
| RHEL 7                            | Node.js 14 from Software Collections  |
| Microsoft Windows Server 2012 R2  | Node.js 14 from the Node.js project  |
| Microsoft Windows Server 2016     | Node.js 14 from the Node.js project  |
| Microsoft Windows 10              | Node.js 14 from the Node.js project  |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Mozilla Firefox
  Note:  Microsoft Internet Explorer is no longer supported for use with Broker consoles.

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system                  | Python version |
| --------------------------------- | -------------- |
| RHEL 8                            | Python 3.6     |
| RHEL 7                            | Python 3.6     |
| Microsoft Windows Server 2012 R2  | Python 3.6 or 3.8     |
| Microsoft Windows Server 2016     | Python 3.6 or 3.8    |
| Microsoft Windows 10 Professional | Python 3.6 or 3.8    |


####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version                        |
| --------------------------------- | ----------------------------------- |
| RHEL 8                            | .NET Core 3.1                       |
| RHEL 7                            | .NET Core 3.1                       |
| Microsoft Windows Server 2012 R2  | .NET Core 3.1 or .NET Framework 4.7 |
| Microsoft Windows Server 2016     | .NET Core 3.1 or .NET Framework 4.7 |
| Microsoft Windows 10 Professional | .NET Core 3.1 or .NET Framework 4.7 |


* Note .NET Core is not supported by the NMS client

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |


####AMQ Pool Support

The following clients support the use of the AMQ Pool library

+ AMQ JMS Client
+ AMQ Core Protocol JMS
+ AMQ OpenWire JMS

Note:  The AMQ Pool library is supported with these clients when used on OS and JVM combinations that are supported by the client.

##  Red Hat AMQ Clients 2.10 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

[Previous Clients Releases](https://access.redhat.com/articles/5043041)

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                            |
| --------------------------------- | ------------------------ | ---------------------------------------------- |
| RHEL 8                            | X86_64                   | OpenJDK 11, Oracle JDK 11, IBM JDK 11 |
| RHEL 7                            | x86_64                   | OpenJDK 11, Oracle JDK 11, or IBM JDK 11          |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 11                                      |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 11                                   |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 11                                   |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 11                                  |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 11                                   |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 8 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | Yes      |
| RHEL 7 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | Yes      |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | Yes                            | Yes                      | No       |
| Microsoft Windows Server 2016     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | Yes                            | Yes                      | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                            |
| -------------------------------- | ------------------------------ |
| RHEL 8                           | OpenJDK 11, Oracle JDK 11, IBM JDK 11 |
| RHEL 7                           | OpenJDK 11 or Oracle JDK 11, IBM JDK 11      |
| Microsoft Windows Server 2012 R2 | Oracle JDK 11                   |
| IBM AIX 7.1                      | IBM JDK 11                      |
| Solaris 10 and 11                | Oracle JDK 8                   |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 8                            | GNU C++                      | Compiling as C++11          |
| RHEL 7                            | GNU C++                      | Compiling as C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++11 |
| Microsfot Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                   |
| --------------------------------- | ------------------------------------ |
| RHEL 8                            | Node.js 10                           |
| RHEL 7                            | Node.js 6 & 8 from Software Collections  |
| Microsoft Windows Server 2012 R2  | Node.js 10 from the Node.js project  |
| Microsoft Windows Server 2016     | Node.js 10 from the Node.js project  |
| Microsoft Windows 10              | Node.js 10 from the Node.js project  |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Mozilla Firefox
  Note:  Microsoft Internet Explorer is no longer supported for use with Broker consoles.

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system                  | Python version |
| --------------------------------- | -------------- |
| RHEL 8                            | Python 3.6     |
| RHEL 7                            | Python 3.6     |
| Microsoft Windows Server 2012 R2  | Python 3.6 or 3.8     |
| Microsoft Windows Server 2016     | Python 3.6 or 3.8    |
| Microsoft Windows 10 Professional | Python 3.6 or 3.8    |


####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version                        |
| --------------------------------- | ----------------------------------- |
| RHEL 8                            | .NET Core 3.1                       |
| RHEL 7                            | .NET Core 3.1                       |
| Microsoft Windows Server 2012 R2  | .NET Core 3.1 or .NET Framework 4.7 |
| Microsoft Windows Server 2016     | .NET Core 3.1 or .NET Framework 4.7 |
| Microsoft Windows 10 Professional | .NET Core 3.1 or .NET Framework 4.7 |


* Note .NET Core is not supported by the NMS client

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |

##  Red Hat AMQ Clients 2.7 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

[Previous Clients Releases](https://access.redhat.com/articles/5043041)

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                            |
| --------------------------------- | ------------------------ | ---------------------------------------------- |
| RHEL 8                            | X86_64                   | OpenJDK 8, OpenJDK 11, Oracle JDM 8, IBM JDK 8 |
| RHEL 7                            | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8          |
| RHEL 6                            | x86 or x86_64            | OpenJDK 8 or Oracle JDK 8                      |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 8                                      |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 8                                   |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 8                                   |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 8                                   |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 8                                   |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 8 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | Yes      |
| RHEL 7 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | Yes      |
| RHEL 6 x86_64                     | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | No       |
| RHEL 6 x86                        | Yes                     | Yes                     | No                                    | Yes                           | No                       | No       |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows Server 2016     | Yes                     | Yes                     | Yes                                   | Yes                           | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                            |
| -------------------------------- | ------------------------------ |
| RHEL 8                           | OpenJDK 8 or 11, Oracle JDK 11 |
| RHEL 7                           | OpenJDK 8 or Oracle JDK 8      |
| RHEL 6                           | OpenJDK 8 or Oracle JDK 8      |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8                   |
| IBM AIX 7.1                      | IBM JDK 8                      |
| Solaris 10 and 11                | Oracle JDK 8                   |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 8                            | GNU C++                      | Compiling at C++11          |
| RHEL 7                            | GNU C++                      | Compiling as C++03 or C++11 |
| RHEL 6                            | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsfot Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++02 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                   |
| --------------------------------- | ------------------------------------ |
| RHEL 8                            | Node.js 10                           |
| RHEL 7                            | Node.js 6 from Software Collections  |
| RHEL 6                            | Node.js 06 from Software Collections |
| Microsoft Windows Server 2012 R2  | Node.js 10 from the Node.js project  |
| Microsoft Windows Server 2016.    | Node.js 10 from the Node.js project  |
| Microsoft Windows 10 Professional | Node.js 10 from the Node.js project  |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system                  | Python version |
| --------------------------------- | -------------- |
| RHEL 8                            | Python 3.6     |
| RHEL 7                            | Python 2.7     |
| RHEL 6                            | Python 2.6     |
| Microsoft Windows Server 2012 R2  | Python 3.6     |
| Microsoft Windows Server 2016     | Python 3.6     |
| Microsoft Windows 10 Professional | Python 3.6     |


####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version                        |
| --------------------------------- | ----------------------------------- |
| RHEL 8                            | .NET Core 3.1                       |
| RHEL 7                            | .NET Core 3.1                       |
| Microsoft Windows Server 2012 R2  | .NET Core 2.1 or .NET Framework 4.5 |
| Microsoft Windows Server 2016.    | .NET Core 2.1 or .NET Framework 4.5 |
| Microsoft Windows 10 Professional | .NET Core 2.1 or .NET Framework 4.5 |


* Note .NET Core is not supported by the NMS client

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |

## Red Hat AMQ Clients 2.6 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                   |
| --------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                            | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                       | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                            | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                         | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 6 and 7                      | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes      |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 2016            | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| HP-UX 11i                         | Yes                     | No                      | No                                    | No                            | No                       | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                      | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsoft Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++02 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                     |
| --------------------------------- | -------------------------------------- |
| RHEL 6 and 7                      | Node.js 0.10 from Software Collections |
| Microsoft Windows Server 2012 R2  | Node.js 4 from the Node.js project     |
| Microsoft Windows Server 2016.    | Node.js 4 from the Node.js project     |
| Mircoroft Windows 10 Professional | Node.js 4 from the Node.js project     |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version                        |
| --------------------------------- | ----------------------------------- |
| Microsoft Windows Server 2012 R2  | .NET Core 2.0 or .NET Framework 4.5 |
| Microsoft Windoes Server 2016.    | .NET Core 2.0 or .NET Framework 4.5 |
| Microsoft Windows 10 Professional | .NET Core 2.0 or .NET Framework 4.5 |

* Note .NET Core is not supported by the NMS client

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |



## Red Hat AMQ Clients 2.5 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                   |
| --------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                            | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                       | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                            | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                         | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 6 and 7                      | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes      |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 2016            | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| HP-UX 11i                         | Yes                     | No                      | No                                    | No                            | No                       | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                      | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsfot Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++02 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                     |
| --------------------------------- | -------------------------------------- |
| RHEL 6 and 7                      | Node.js 0.10 from Software Collections |
| Microsoft Windows Server 2012 R2  | Node.js 4 from the Node.js project     |
| Microsoft Windows Server 2016.    | Node.js 4 from the Node.js project     |
| Mircoroft Windows 10 Professional | Node.js 4 from the Node.js project     |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version                        |
| --------------------------------- | ----------------------------------- |
| Microsoft Windows Server 2012 R2  | .NET Core 2.0 or .NET Framework 4.5 |
| Microsoft Windoes Server 2016.    | .NET Core 2.0 or .NET Framework 4.5 |
| Microsoft Windows 10 Professional | .NET Core 2.0 or .NET Framework 4.5 |

* Note .NET Core is not supported by the NMS client

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |



___
## Red Hat AMQ Clients 2.4 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                   |
| --------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                            | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                       | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                            | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                         | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 6 and 7                      | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes      |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 2016            | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| HP-UX 11i                         | Yes                     | No                      | No                                    | No                            | No                       | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                      | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsfot Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++02 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                     |
| --------------------------------- | -------------------------------------- |
| RHEL 6 and 7                      | Node.js 0.10 from Software Collections |
| Microsoft Windows Server 2012 R2  | Node.js 4 from the Node.js project     |
| Microsoft Windows Server 2016.    | Node.js 4 from the Node.js project     |
| Mircoroft Windows 10 Professional | Node.js 4 from the Node.js project     |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version       |
| --------------------------------- | ------------------ |
| Microsoft Windows Server 2012 R2  | .NET Framework 4.5 |
| Microsoft Windoes Server 2016.    | .NET Framework 4.5 |
| Microsoft Windows 10 Professional | .NET Framework 4.5 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |



___

## Red Hat AMQ Clients 2.3 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                  | Architecture             | JVM                                   |
| --------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                            | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                       | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                            | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                         | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                       | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2  | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows Server 2016     | x86_64                   | Oracle JDK 8                          |
| Microsoft Windows 10 Professional | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                 | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                  | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| --------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 6 and 7                      | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes      |
| Microsoft Windows Server 2012 R2  | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 2016            | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| Microsoft Windows 10 Professional | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| HP-UX 11i                         | Yes                     | No                      | No                                    | No                            | No                       | No       |
| IBM AIX 7.1                       | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                 | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                  | Compiler                     | Standard                    |
| --------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                      | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2  | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2016     | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |
| Microsfot Windows 10 Professional | Microsoft Visual Studio 2013 | Compiling as C++02 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                  | JavaScript runtime                     |
| --------------------------------- | -------------------------------------- |
| RHEL 6 and 7                      | Node.js 0.10 from Software Collections |
| Microsoft Windows Server 2012 R2  | Node.js 4 from the Node.js project     |
| Microsoft Windows Server 2016.    | Node.js 4 from the Node.js project     |
| Mircoroft Windows 10 Professional | Node.js 4 from the Node.js project     |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                  | .NET version       |
| --------------------------------- | ------------------ |
| Microsoft Windows Server 2012 R2  | .NET Framework 4.5 |
| Microsoft Windoes Server 2016.    | .NET Framework 4.5 |
| Microsoft Windows 10 Professional | .NET Framework 4.5 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |



___
## Red Hat AMQ Clients 2.2 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                 | Architecture             | JVM                                   |
| -------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                           | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                      | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                           | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                        | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                      | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2 | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                 | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| -------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 6 and 7                     | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes      |
| Microsoft Windows Server 2012 R2 | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| HP-UX 11i                        | Yes                     | No                      | No                                    | No                            | No                       | No       |
| IBM AIX 7.1                      | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                | Yes                     | No                      | No                                    | No                            | No                       | No       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                 | Compiler                     | Standard                    |
| -------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                     | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2 | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                 | JavaScript runtime                     |
| -------------------------------- | -------------------------------------- |
| RHEL 6 and 7                     | Node.js 0.10 from Software Collections |
| Microsoft Windows Server 2012 R2 | Node.js 4 from the Node.js project     |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                 | .NET version       |
| -------------------------------- | ------------------ |
| Microsoft Windows Server 2012 R2 | .NET Framework 4.5 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client       | Wire Protocol     |
| ------------ | ----------------- |
| AMQ JMS      | Core Protocol     |
| AMQ OpenWire | OpenWire Protocol |

___


## Red Hat AMQ Clients 2.1 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.  Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                 | Architecture             | JVM                                   |
| -------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                           | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                      | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                           | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                        | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                      | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2 | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                 | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby |
| -------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | -------- |
| RHEL 7                           | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes      |
| RHEL 6                           | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | No       |
| Microsoft Windows Server 2012 R2 | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No       |
| HP-UX 11i                        | Yes                     | No                      | No                                    | No                            | No                       | No       |
| IBM AIX 7.1                      | Yes                     | No                      | No                                    | No                            | No                       | No       |
| Solaris 10 and 11                | Yes                     | No                      | No                                    | No                            | No                       | No       |



###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                 | Compiler                     | Standard                    |
| -------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                     | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2 | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                 | JavaScript runtime                          |
| -------------------------------- | ------------------------------------------- |
| RHEL 6 and 7                     | Node.js 4, 6, & 8 from Software Collections |
| Microsoft Windows Server 2012 R2 | Node.js 4, 6, & 8  from the Node.js project |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system                 | Python version    |
| -------------------------------- | ----------------- |
| RHEL 6 and 7                     | Python 2.6 or 2.7 |
| Microsoft Windows Server 2012 R2 | Python 2.7        |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                 | .NET version                      |
| -------------------------------- | --------------------------------- |
| Microsoft Windows Server 2012 R2 | .NET Framework 4.5, .NET Core 2.0 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |

___

## Red Hat AMQ Clients 2.0 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions. Note:  Clients are backward compatible and supported on the latest released and supported version of AMQ 6.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                 | Architecture             | JVM                                   |
| -------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                           | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                      | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                           | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                        | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                      | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2 | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                 | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) | AMQ Ruby* |
| -------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ | --------- |
| RHEL 7                           | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | Yes       |
| RHEL 6                           | Yes                     | Yes                     | Yes                                   | Yes                           | No                       | No        |
| Microsoft Windows Server 2012 R2 | Yes                     | Yes                     | Yes                                   | No                            | Yes                      | No        |
| HP-UX 11i                        | Yes                     | No                      | No                                    | No                            | No                       | No        |
| IBM AIX 7.1                      | Yes                     | No                      | No                                    | No                            | No                       | No        |
| Solaris 10 and 11                | Yes                     | No                      | No                                    | No                            | No                       | No        |

*Developer Preview only not suitable for production use.

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                 | Compiler                     | Standard                    |
| -------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6 and 7                     | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2 | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                 | JavaScript runtime                          |
| -------------------------------- | ------------------------------------------- |
| RHEL 6 and 7                     | Node.js 4, 6, & 8 from Software Collections |
| Microsoft Windows Server 2012 R2 | Node.js 4, 6, & 8  from the Node.js project |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                 | .NET version                      |
| -------------------------------- | --------------------------------- |
| Microsoft Windows Server 2012 R2 | .NET Framework 4.5, .NET Core 2.0 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |

___


## Red Hat AMQ Clients 1.2 {#clients}

AMQ Clients are supported for use on the following operating systems, architectures, and JVM versions.

**Not** all clients are supported on all operating systems. Specific client support is documented in the section titled [Specific supported clients and OSs](#client_os).

| Operating system                 | Architecture             | JVM                                   |
| -------------------------------- | ------------------------ | ------------------------------------- |
| RHEL 6                           | x86                      | OpenJDK 8 or Oracle JDK 8             |
| RHEL 6 or 7                      | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| RHEL 7                           | x86_64                   | OpenJDK 8, Oracle JDK 8, or IBM JDK 8 |
| HP-UX 11i                        | x86_64                   | HP JVM 8                              |
| IBM AIX 7.1                      | x86_64                   | IBM JDK 8                             |
| Microsoft Windows Server 2012 R2 | x86_64                   | Oracle JDK 8                          |
| Solaris 10 and 11                | x86, x86_64, or Sparc 64 | Oracle JDK 8                          |

Note: Earlier versions of the JDK are not supported.

###Specific supported clients and OSs {#client_os}

The table below lists the supported operating systems for each AMQ Client. Additional information about specific clients is documented in subsequent sections.

| Operating system                 | [AMQ JMS](#jms_details) | [AMQ C++](#cpp_details) | [AMQ JavaScript](#javascript_details) | [AMQ Python](#python_details) | [AMQ .NET](#net_details) |
| -------------------------------- | ----------------------- | ----------------------- | ------------------------------------- | ----------------------------- | ------------------------ |
| RHEL 6 and 7                     | Yes                     | Yes                     | Yes                                   | Yes                           | No                       |
| Microsoft Windows Server 2012 R2 | Yes                     | Yes                     | Yes                                   | No                            | Yes                      |
| HP-UX 11i                        | Yes                     | No                      | No                                    | No                            | No                       |
| IBM AIX 7.1                      | Yes                     | No                      | No                                    | No                            | No                       |
| Solaris 10 and 11                | Yes                     | No                      | No                                    | No                            | No                       |

###AMQ JMS details {#jms_details}

The AMQ JMS client is supported on the following OSs and JVMs.

| Operating system                 | JVM                       |
| -------------------------------- | ------------------------- |
| RHEL 6 and 7                     | OpenJDK 8 or Oracle JDK 8 |
| Microsoft Windows Server 2012 R2 | Oracle JDK 8              |
| HP-UX 11i                        | HP-UX JVM 8               |
| IBM AIX 7.1                      | IBM JDK 8                 |
| Solaris 10 and 11                | Oracle JDK 8              |

Note: Earlier versions of the JDK are not supported.

####Standards and network protocols

+ Version 2.0 of the [Java Message Service](https://jcp.org/en/jsr/detail?id=343) API
+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Version 1.0 of the AMQP JMS Mapping
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ C++ details {#cpp_details}

The AMQ C++ client is supported on the following OSs with the compilers and standards that are listed.

| Operating system                 | Compiler                     | Standard                    |
| -------------------------------- | ---------------------------- | --------------------------- |
| RHEL 6(64 bit only) & 7          | GNU C++                      | Compiling as C++03 or C++11 |
| Microsoft Windows Server 2012 R2 | Microsoft Visual Studio 2013 | Compiling as C++03 or C++11 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ JavaScript details {#javascript_details}

The AMQ JavaScript client is supported on the following OSs and JavaScript runtimes.

| Operating system                 | JavaScript runtime                                  |
| -------------------------------- | --------------------------------------------------- |
| RHEL 6 (64 bit only)             | Node.js 0.10 from Software Collections              |
| RHEL 7                           | Node.js 0.10 or Node.js 4 from Software Collections |
| Microsoft Windows Server 2012 R2 | Node.js 4 from the Node.js project                  |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

####Supported browsers {#javascript_browsers}

Supported browsers include the following:

+ Google Chrome
+ Microsoft Internet Explorer
+ Mozilla Firefox

###AMQ Python details {#python_details}

The AMQ Python client is supported on the following OSs and languages.

| Operating system | Python version    |
| ---------------- | ----------------- |
| RHEL 6 and 7     | Python 2.6 or 2.7 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Versions 1.0, 1.1, and 1.2 of the [Transport Layer Security](https://tools.ietf.org/html/rfc5246) (TLS) protocol, the successor to SSL
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

###AMQ .NET details {#net_details}

The AMQ .NET client is supported with the following OS and runtime.

| Operating system                 | .NET version       |
| -------------------------------- | ------------------ |
| Microsoft Windows Server 2012 R2 | .NET Framework 4.5 |

####Standards and network protocols

+ Version 1.0 of the [Advanced Message Queueing Protocol](http://www.amqp.org/) (AMQP)
+ Modern [TCP](https://tools.ietf.org/html/rfc793) with [IPv6](https://tools.ietf.org/html/rfc2460)

[1] Red Hat expects that customers will remain on a supported environment. In the event that a JVM, operating system, database, etc., or its version is no longer supported by its vendor, Red Hat may be limited in its ability to provide support and may require you to reproduce the issue in a supported environment for continued assistance.

####XA Transaction support

The following clients support XA transactions.

| Client                | Wire Protocol     |
| --------------------- | ----------------- |
| AMQ Core Protocol JMS | Core Protocol     |
| AMQ OpenWire JMS      | OpenWire Protocol |

___


