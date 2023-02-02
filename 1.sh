row_num=$(cat file.txt | wc -l)
echo $row_num
sed -n '9p' file.txt
if [ $row_num -lt 9 ];then
  echo " 小于10行 "
else
  sed -n '10p' file.txt
fi