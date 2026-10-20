# Storage Estimator
size_mb = float(input("Enter file size in MB: "))
count = int(input("Enter number of files: "))

total_mb = size_mb * count
total_kb = total_mb * 1024

print("Total size (MB):", total_mb)
print("Total size (KB):", total_kb)
