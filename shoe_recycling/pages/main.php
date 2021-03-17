<div id="main">
            <?php
                if(isset($_GET['manage'])){
                    $tam =$_GET['manage'];
                } else{
                    $tam = '';
                }
                if($tam=='Sale'){
                    include("main/sale.php");
                } elseif($tam=='Men'){
                    include("main/Men.php");
                }elseif($tam=='Women'){
                    include("main/Women.php");
                }elseif($tam=='About_us'){
                    include("main/about_us.php");
                }elseif($tam=='detail'){
                    include("main/detail_product.php");
                }else{
                    include("main/index.php");
                }
                
            ?>
            
        </div>