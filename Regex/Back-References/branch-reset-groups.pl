$Test_String = <STDIN> ;

$Regex_Pattern = '^[\d]{2}(---|-|:|\.| ?)\d{2}\1\d{2}\1\d{2}$';
if($Test_String =~ /$Regex_Pattern/){
    print "true";
} else {
    print "false";
}