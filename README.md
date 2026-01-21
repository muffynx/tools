# tools
# Initialize a new Git repository
```
git init  
```
# Stage all files
```
git add .  
```
# Commit the changes
```
git commit -m "Initial commit"  
```
# Add remote repository
```
git remote add origin https://github.com/muffynx/.git  
```
# Rename branch to 'main' (if needed)
```
git branch -M main  
```

# Push the code to GitHub
```
git push -u origin main  

```
เขียนทับ
```
git push -u origin main --force 
```
remove origin
```
git remote remove origin 
```

show origin
```
git remote show origin
```
git pull origin master
วิธีแก้

เช็ค branch ที่มีใน remote ก่อน

git fetch origin
git branch -r


จะเห็นรายการเช่น

origin/main
origin/dev


ถ้า branch หลักคือ main ให้ใช้

git pull origin main


วิธีที่ 2: ทิ้งของ local แล้วใช้ของ GitHub ทั้งหมด

ใช้เมื่อ local ยังไม่สำคัญ
```
git fetch origin
git reset --hard origin/main
```

⚠️ โค้ดในเครื่องจะหายหมด

✅ วิธีที่ 3: เอา local ไปทับ GitHub

ใช้เมื่อ local คือของจริง
```
git push origin main --force
```

⚠️ โค้ดบน GitHub จะโดนเขียนทับ
