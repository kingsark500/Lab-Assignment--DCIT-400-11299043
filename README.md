# Lab-Assignment--DCIT-400-11299043

 # LAB 1 SETUP ENVIRONMENT REPORT
 In this lab assignment, the Smart Python Agent Development Environment (SPADE) was used to set up an intelligent agent development environment and implement a simple autonomous agent. Every development activity was carried out within GitHub Codespaces, which offer a consistent, browser-based programming environment without requiring local installation.

 Python version 3.9 was confirmed to be present in the Codespaces environment, meeting SPADE's criteria. Using the Python package manager (pip), the SPADE framework was installed and successfully imported, indicating correct installation. SPADE facilitates the creation of intelligent beings through message-based communication and asynchronous behaviours.

 For communication, SPADE agents usually depend on an XMPP server. However, system-level services like Prosody and ejabberd are not supported by GitHub Codespaces. A public XMPP server (xmpp.jp) was utilised to overcome this restriction. For agent authentication, a free XMPP account was made with a working Jabber ID (JID) and password. This method works well in cloud-based setups and is compatible with SPADE.

 Python was used to create and run a simple SPADE agent. After establishing a successful connection with the xmpp.jp server, the agent carried on a cyclic behaviour that displayed messages to the terminal on a regular basis. The agent lifespan, connectivity, and autonomous execution were all verified by the repeated output.

 A functional intelligent agent platform was successfully created in this lab, providing a strong basis for later research on perception, communication, coordination, and multi-agent system design.
