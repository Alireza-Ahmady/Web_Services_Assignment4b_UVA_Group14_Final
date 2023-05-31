## Web_Services_Assignment4b_UVA_Group14_Final

## 1- Import packages:
We assume that you have already installed and configured Brane by following the documentation of the Brane Framework.
Open a terminal that has access to the brane-command and then run:
```bash 
brane import Alireza-Ahmady/Web_Services_Assignment4b_UVA_Group14_Final -c packages/compute/container.yml
brane import Alireza-Ahmady/Web_Services_Assignment4b_UVA_Group14_Final -c packages/visualization/container.yml
```
## 2- Obtaining data:
Navigate to the folder of the training and testing datasets, then run the following command:
```bash 
brane data build ./data.yml
```
## 3- Local execution: Run the following command to execute the pipeline:
```bash
brane run pipeline.bs
```
