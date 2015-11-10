<?php
     	$url = $_GET["url"];
        $fp = fopen('url.txt', 'w');
        fwrite($fp, $url);
        fclose($fp);

	$command = escapeshellcmd('python downloadImage.py');
$output = shell_exec($command);
echo $output;
?>
