## Web_Services_Assignment4b_UVA_Group14_Final

## 1- Link to the repository:
```bash 
https://github.com/Alireza-Ahmady/Web_Services_Assignment4b_UVA_Group14_Final
```
## 2-  Brief description of our experience of working with BRANE:
The overall experience with Brane can be expressed as “a lot of challenges leading to multiple learnings”. During the initial setup and configuration of BRANE we faced multiple challenges including setting up of control and worker node, ensuring data and packages are flowing to the worker node, configuration of security certificates and to ensure the functions are executed via remote worker node. We were able to resolve all of the issues with the help of TA but one of the key observations is lack of documentation with regards to BRANE. If we compare BRANE to any other programming language or practice the documentation, knowledge base and the related threads provides debugging assistance which is currently limited for BRANE and can be improved.
Once we configured the BRANE framework, we re-packaged our python notebook to be able to work with BRANE into functions, compute and visualisation packages. Although in this process we did not face many critical challenges, but the key learning in understanding BRANE only came during the final steps of the process. The key learning for us was that we can create modular, re-usable functions which can then be used in any similar context without having to know the detailed execution of the function. For e.g. when we create clean null function to remove all null value, the function works independently without any coupling with the titanic objective we are working on. The function takes dataset as an input, clean the null values and return an cleaned dataset. It was interesting to understand this modularity and reusability as a concept especially in relation to different roles and responsibilities including the segregation of responsibilities between different roles like data scientist and software engineer. The data scientist would be able to work with different reusable functions and do their job without having to understand or implement the business logic in python like language to clean the data or process the data which a software engineer can do better and make it reusable without having to align it with the context the function would be used.
The key observation coming out of this for us is that the usage of BRANE would be more easier and friendly for data scientists if the library or repository of reusable functions is growing like an app store which in turn would enable more software engineer’s to contribute to the library.

## 3- Contributors and Tasks:
| Name              | Task          |
|-------------------|---------------|
| Alireza Ahmady    | Primarily focused on coding, setting up the Brane environment, creating packages, and implementing various functionalities. Also conducted testing to ensure code functionality and reviewed the document, making changes to contribute to the report.|
| Abhilash M        | Mainly focused on testing and debugging the implementation, as well as creating presentations. Also contributed to setting up the Brane environment and actively worked on the documentation. |
| Niveditha Govindu | Mainly focused on the report, while also contributing to testing, debugging, and understanding the machine learning algorithm. |
