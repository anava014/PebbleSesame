<?php 
	if(isset($_GET['trigger']) && $_GET['trigger'] == 1) {
		exec('gpio write 7 0');
		usleep(1000000);
		exec('gpio write 7 1');
	}
?>
