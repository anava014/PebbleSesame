<?php
	
	$command = $_GET["command"];
        $fp = fopen("request.txt", "w");
        fwrite($fp, $command);
        fclose($fp);
        echo Test;
	
?>


