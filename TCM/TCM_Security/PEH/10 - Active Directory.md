# Active Directory
## What is Active Directory?

- A directory services developed by microsoft to manage windows domain networks
- Stores information related to objects, such as Computer, Users, Printers etc.
	- Like a phonebook to windows
- Authentication using Kerberos tickets
	- Non-Windows devices, like Linux machines, firewalls, etc. can also authenticate to Active Directory via RADIUS or LDAP

- Active Directory is the most commonly used identity management service in the world
	- 95% of Fortune 1000 companies implement the service in their networks
- Can be exploited without ever attacking patchable exploits.
	- Instead, we abuse features, trusts, componentes and more.
	
---



## Physical Active Directory Components

### Domain Controller
The domain controller is a server with the AD DS server role installed that has specifically been promoted to a domain controller

#### Domain Controllers
- Host a copy of the AD DS directory store
- Provide authentication and authorization services
- Replicate updates to toher domain conrollers in the domain and forest
- Allow adminsitrative access to manage user accounts and network resources

### AD DS Data Store
The AD DS data store contains the database files and processes that store and manage directory information for user, services and applications

#### The AD DS data store
- Consist of the Ntds.dit file
- Is stored by default in the %SystemRoot%\NTDS folder on all domain controllers
- Is accessible only thorug the domain controllers processes and protocols

---

## Logical Active Directory Components
### AD DS Schema:
-	Defines every types of objects that can be stored in the directory
-	Enforces rules regarding objects creation and configuration

| Object Types | Function | Examples|
|-----|----|----|
| Class Object | What objects can be created in the directory | - User <br> - Computer|
| Attribute Object | Information can be attached to an object | - Display name|


---
### Domains
Domains are used to group and manage objects in an organization
#### Domains
-	An administrative boundary for the applying policies to group of objects
-	A replication boundary for the replicating data between domain controllers
-	An authentication and authorization boundary that provides a way to limit the scope of access to resources
---
### Trees
The domain tree is a hierarchy of domains in AD DS
~~~bash
                                  contoso.com
                                    /     \ 
                                   /       \      
                     emea.contoso.com     na.contoso.com
~~~
   All domains in the tree:
      - Share a contiguos namespace with the parent domain
      - Can have additional child domains
      - By default create a two-way transitive trust with other domains

---
### Forests
   A forest is a collection of one or more domain trees
      Forests:
        - Share a common schema
        - Share a common configuration partition
        - Share a common global catalog to enable searching
        - Enable trusts between all domains in the forest
        - Share the Enterprise Admins and Schema Admins groups

---
### Organizaional Units (Ous)
   OUs are Active Directory containers that can contain users, groups, computers, and other OUs
      OUs are used to:
        - Represent your organization hierarchically and logically
        - Manage a collection of objects in a consistent way
        - Delegate permission to administrative groups of objects
        - Apply policies

---
### Trusts
   Trusts provide a mechanism for users to gain access to resources in another domain
      Trusts:
        - All domains in a forest trust all other domains in the forest
        - Trusts can extend outside the forest

| Types of Trusts | Description | Diagram |
| --- | --- | --- |
| Directional |The trust direction flows from trusting domain to trusted domain | ![[directionalTrust.png]]|
| Transitive | The trust relationship is extended beyond a two-domain trust to include other trusted domains | ![[transitiveTrust.png]]|

---
### Objects

| Object | Description |
|-------|--------|
|  User | - Enables network resource access for user|
|InetOrgPerson |  - Similar to user account <br> - Used for compatibility with other directory services  |
|  Contacts | - Used primarly to assign e-mail addresses to external users <br> - Does not enable network access |
| Groups | - Used to simplify the administration of access control |
| Computers | - Enables authentication and auditing of computer access to resources
| Printers | - Used to simplify the process of locating and connecting to printers |
| Shared Folders |- Enables users to search for shared folders based properties |


---
>Domains -> Tree(parent domains, children domains) -> Forest(multiple trees)
Domain  <- OUs <- Objects
Cross forests(cross domains) <-> Trusts 

---