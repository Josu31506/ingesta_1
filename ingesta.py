import boto3

ficheroUpload = "data.csv"
nombreBucket = "farmacia-ds"

s3 = boto3.client('s3')
response = s3.upload_file(ficheroUpload, nombreBucket, 
                          "medicinas/" + 
                          ficheroUpload)
print(response)

print("Ingesta completada")
