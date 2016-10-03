$Test_String = <STDIN> ;

$Regex_Pattern = '^tac(tac(tic)?)*$';
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}