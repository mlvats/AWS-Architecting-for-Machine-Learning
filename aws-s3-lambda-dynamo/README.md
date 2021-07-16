## Security Price Loading Project

The task is to implement a simplified version of the daily loading of security price files into a DynamoDB table.  

1. Whenever a data file is dropped into the S3 bucket named security-price-12345, the corresponding event should invoke a lambda function automatically  
2. The lambda function should read the file and load it into a DynamoDB table named security-price-12345-table.  
3. The file should have three columns: id, ticker and price.   
4. The table should have four columns: id, ticker, price and loaded timestamp.  
5. The whole solution should be deployed through a CloudFormation template.  
    - DynamoDB table should be created from the template     
    - Lambda function should be created from the template  
    - All the event handling / triggering mechanism should be created from the template  
       
---    
# S3-to-lambda-to-DynamoDB

Automatically imports a JSON array from an S3 object into Amazon DynamoDB, using Lambda Function
    
---  
## AWS Serverless Application Model (AWS SAM)  
- AWS SAM templates are an extension of AWS CloudFormation templates, with some additional components that make them easier to work with
- We use the AWS SAM specification to define your serverless application.  
- template.yaml: Contains the AWS SAM template that defines our application's AWS resources.

---  
## Deploy
go to folder : ` aws-s3-lambda-dynamo\v1`   
guided deploy : `sam deploy --guided`  

```bash
aws s3 cp data/securitydata.json s3://security-price-12345d/securitydata.json  
aws s3 cp data/securitydata_1.json s3://security-price-12345d/securitydata_1.json
```
---
## Cleanup

```bash
aws s3 rm  s3://security-price-12345d/securitydata.json
aws s3 rm  s3://security-price-12345d/securitydata_1.json

aws cloudformation delete-stack --stack-name sam-app

```


  
 

