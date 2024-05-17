<h1>Robot Kol Otomatik Rulman Besleme Sistemi</h1>

<p>Bu projeyi, <i>Özsoy Asansör Makina A.Ş.</i> için geliştirdim. Projede, enjeksiyon makinesine bağlı bir robot kol, enjeksiyon makinesindeki kalıbın ilgili noktalarına rulmanlar yerleştirmektedir. Robot kolun her seferinde yeni rulmanları alabilmesi için otomatik bir besleme sistemine ihtiyaç duyulmaktaydı. Bu ihtiyacı karşılamak amacıyla, sistemi baştan sona tasarlayıp gerçekleştirdim. Bu süreçte yazılım geliştirme, devre kartı tasarımı, üretimi, dizgi işlemi ve sistemin montajı dahil tüm aşamaları kendim üstlendim.</p>

<h2>Sistem Bileşenleri</h2>
<ul>
  <li><b>Sensör Sistemi:</b> Raylardaki rulmanların sayısını tespit eden, pistonların üzerine rulmanın geldiğini tespit eden ve pistonlara yükselme komutunu gönderen endüktif sensörler bulunmaktadır. Aynı zamanda robot kolun gelip gittiğini algılamayı sağlayan kapasitif sensör bulunmaktadır.</li>
  <li><b>Rulman Kaldırma Mekanizması:</b> Robot kolun rulmanları kolayca alabilmesi için rulmanları havaya kaldıran bir mekanizma bulunmaktadır. Bu mekanizma, rulmanların yuvalarda olduğunu sensörler ile tespit ederek rulmanları yükseltmesi için pistonlara sinyal göndererek yükselmesini sağlamaktadır. Ayrıca robot kolun geldiğini ve gittiğini tespit eden kapasitif sensör pistonlara yuvaları indirme sinyalini gördermektedir.</li>
  <li><b>Motor ve Yönlendirme Mekanizması:</b> Raylar üzerindeki rulman sayısı azaldığında rayların başı ve sonunda bulunan endüktif sensörler ile bunu tespit ederek, motorun dönüş hareketini başlatarak yeni rulmanları raylara yönlendiren bir sistem mevcuttur. Bu mekanizma, rulmanlar azaldığında çalışarak rulmanların raylarda hazır bulunmasını sağlar.</li>
  <li><b>Rulman Haznesi:</b> Rulmanların tutulduğu ve depolandığı bir hazne bulunuyor. Bu hazne, belirli zaman aralığında rulmanları raylara yönlendiren motorun üst bölümüne rulman dolmasını sağlar.</li>
</ul>

<p>Bu projenin yazılım kısmında, endüktif ve kapasitif sensör verilerinin işlenmesi, kontaktör ile motor kontrolü, solenoid vana ile pnömatik piston kontrolü ve genel sistem entegrasyonu üzerinde yoğunlaştım.</p>

<p>Devre kartı tasarımında, sensörler ve motor kontrolü için gerekli devre elemanlarını seçerek, işlevsel ve güvenilir bir kart oluşturmayı başardım. Üretim aşamasında masaüstü CNC ile devre kartını kazıdım sonrasında ise komponentlerin dizgi işlemini ve testlerini gerçekleştirdim.</p>

<p><b>Sonuç:</b> Bu proje, robot kolun rulman besleme sürecini otomatikleştirerek, iş verimliliğini ve doğruluğunu artırmıştır. Bu tür otomasyon sistemleri, endüstriyel süreçlerin optimize edilmesinde önemli bir rol oynamaktadır.</p>
