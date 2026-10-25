storage_gb=float(input("Enter Storage in GB: "))
storage_mb=storage_gb*1024
storage_tb=storage_gb/1024
print('The total storage in MB is: ', storage_mb)
print('The total storage in TB is: ', storage_tb)