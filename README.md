apt update && apt upgrade -y
pkg install git -y
pkg install python -y
cd
rm -rf FB-Cloning-Master
git clone https://github.com/CYBER71ENAFUL/FB-Cloning-Master
cd FB-Cloning-Master
chmod +x *
pip install -r requirements.txt
python tool.py
