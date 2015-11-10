<?php
	$state = $_GET["state"];
	$fp = fopen('currentState.txt', 'w');
	fwrite($fp, $state);
	fclose($fp);
?>