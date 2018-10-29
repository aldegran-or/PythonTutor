bash_prompt_command() {
# How many characters of the $PWD should be kept
pwdmaxlen=25

# Indicate that there has been dir truncation
trunc_symbol=".."

# Store local dir
dir=$(pwd | wc -c)
echo $dir

# Which length to use
#let pwdmaxlen=$(( ( pwdmaxlen < ${#dir} ) ? ${#dir} : pwdmaxlen ))

#NEW_PWD=${PWD/#$HOME/\~}

#local pwdoffset=$(( ${#NEW_PWD} - pwdmaxlen ))

# Generate name
#if [ ${pwdoffset} -gt "0" ]
#then
# NEW_PWD=${NEW_PWD:$pwdoffset:$pwdmaxlen}
# NEW_PWD=${trunc_symbol}/${NEW_PWD#*/}
#fi
}
