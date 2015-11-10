<?php
	$state = $_GET["state"];
	$fp = fopen('doorState.txt', 'w');
	fwrite($fp, $state);
	fclose($fp);
?>
[ec2-user@ip-