bash_prompt_command() {
# How many characters of the $PWD should be kept
pwdmaxlen=25

# Indicate that there has been dir truncation
trunc_symbol=".."

# Store local dir
dir=$(pwd | wc -c)
echo "dirDigit=$dir"
coll=$COLUMNS
}
