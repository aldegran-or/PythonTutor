if [ -f testFunctions.sh ] ; then 
           echo "File found"
	. ./testFunctions.sh
fi
bash_prompt_command
echo " pwdmaxlen = $pwdmaxlen"
echo "columns = $coll"