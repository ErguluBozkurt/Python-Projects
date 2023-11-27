motor_servo ="""
                MOT_PWM_TYPE => Motor PWM tipi: Motor kontrol sinyali için kullanılan PWM tipini belirler.
                MOT_PWM_MIN => Motor PWM minimum değeri: Motorun minimum PWM değerini belirler.
                MOT_PWM_MAX => Motor PWM maksimum değeri: Motorun maksimum PWM değerini belirler.
                MOT_SPIN_ARM => Motorun kalkışta dönme durumu: İHA kalkış sırasında motorların dönüp dönmeyeceğini belirler.
                MOT_SLEW_RATE => Motor hızı değişim hızı: Motor hızının ne kadar hızlı değişebileceğini belirler.
                SERVO1_FUNCTION => Servo 1 fonksiyonu: Servo 1'in hangi işlevi yerine getireceğini belirler.
                SERVO2_FUNCTION => Servo 2 fonksiyonu: Servo 2'nin hangi işlevi yerine getireceğini belirler.
                SERVO3_FUNCTION => Servo 3 fonksiyonu: Servo 3'ün hangi işlevi yerine getireceğini belirler.
                SERVO4_FUNCTION => Servo 4 fonksiyonu: Servo 4'ün hangi işlevi yerine getireceğini belirler.
                SERVO5_FUNCTION => Servo 5 fonksiyonu: Servo 5'in hangi işlevi yerine getireceğini belirler.
            """
telemetry = """
                SR0_** ve SR1_** => Telemetri hızları: İHA'nın veri akış hızını belirler, Örneğin, SR0_RATE, İHA'dan telemetri akışının hızını belirler.
                SERIAL0_** ve SERIAL1_** => Seri bağlantı parametreleri: İHA üzerindeki seri bağlantı noktalarının (UART) konfigürasyonunu belirler, 
                                            Örneğin, SERIAL0_BAUD belirli bir UART bağlantısının baud hızını ayarlar.
                SR0_EXTRA1 ve SR1_EXTRA1 => Ekstra telemetri hızı: Ekstra telemetri akışının hızını belirler.
                SR0_RAWCTRL ve SR1_RAWCTRL => Ham kontrol telemetrisi hızı: İHA'nın kontrol verilerini (RC kanalları gibi) telemetri üzerinden gönderme 
                                              hızını belirler.
                SR0_POSITION ve SR1_POSITION => Konum telemetrisi hızı: İHA'nın konum verilerini telemetri üzerinden gönderme hızını belirler.
                SR0_EXTRA2 ve SR1_EXTRA2 => Ekstra telemetri hızı: İlave telemetri verilerini gönderme hızını belirler.
                SR0_PARAMS ve SR1_PARAMS => Parametre telemetrisi hızı: İHA parametrelerini telemetri üzerinden gönderme hızını belirler.
                SR0_RC_CHAN ve SR1_RC_CHAN => Uzaktan kumanda kanal telemetrisi hızı: Uzaktan kumanda kanal verilerini telemetri üzerinden gönderme hızını 
                                              belirler.
                SR0_STAT ve SR1_STAT => İHA durumu telemetrisi hızı: İHA'nın genel durum bilgilerini telemetri üzerinden gönderme hızını belirler.
                SR0_MISSION ve SR1_MISSION => Görev telemetrisi hızı: İHA görev bilgilerini telemetri üzerinden gönderme hızını belirler. 
            """
camera = """
            CAM_DURATION => Kamera kaydı süresi (saniye): Kamera tarafından gerçekleştirilen bir kayıtın ne kadar süreyle devam edeceğini belirler.
            CAM_MODE => Kamera modu: Kameranın hangi modda çalışacağını belirler, örneğin, fotoğraf çekme veya video kaydı.
            CAM_AUTO_CAPTURE => Otomatik Fotoğraf Çekme: Kamera tarafından belirli bir aralıkta otomatik olarak fotoğraf çekilip çekilmeyeceğini belirler.
            CAM_TRIGG_DIST => Tetikleme Mesafesi: Kamera tarafından otomatik olarak tetiklenmesi için İHA'nın belirli bir mesafeye gitmesi gereken uzaklık.
            CAM_FEEDBACK => Kamera Geri Bildirimi: Kameranın işlem sonrası bilgileri İHA'ya geri bildirip bildirmeyeceğini belirler.
            CAM_FEEDBACK_MODE => Kamera Geri Bildirimi Modu: Kamera geri bildiriminin nasıl yapılacağını belirler, örneğin, video akışı veya görüntü dosyaları.
            CAM_GIMBAL_MODE => Kamera Gimbali Modu: Kamera gimbalının nasıl çalışacağını belirler, örneğin, manuel veya otomatik izleme modu.
            CAM_DURATION => Kamera Kayıt Süresi: Bir video kaydının ne kadar süreyle devam edeceğini belirler.
            CAM_AUTOFOCUS => Otomatik Odaklama: Kameranın otomatik olarak odaklanıp odaklanmayacağını belirler.
            CAM_AUTOFOCUS_DROP => Otomatik Odaklama Azalması: Odak uzaklığının otomatik olarak azaltılma hızını belirler.
        """
move_speed = """
        WPNAV_SPEED => Yol noktası gezinme hızı (m/s): İHA'nın bir yol noktasından diğerine geçerken kullanılacak hızı belirler, Bu, İHA'nın görevi sırasında belirli 
                        bir hızda hareket etmesini sağlar.
        WPNAV_ACCEL => Yol noktası gezinme ivmesi (m/s^2): İHA'nın hızını değiştirmek için kullanılacak ivmeyi belirler, Bu, İHA'nın daha pürüzsüz bir şekilde 
                        hızlanmasını ve yavaşlamasını sağlar.
        LAND_SPEED => İniş hızı (m/s): İHA'nın iniş sırasındaki hızını belirler.
        TECS_SINK_MIN => Minimum iniş hızı (m/s): İHA'nın en düşük iniş hızını belirler.
        TECS_LAND_ARSPD => İnişteki hava hızı (m/s): İniş sırasında İHA'nın hava hızını belirler, İHA'nın rüzgar etkilerine karşı daha dirençli bir iniş gerçekleştirir.
        LOIT_SPEED => Dönüş hızı (m/s): İHA'nın çevresinde dönerken kullanılacak hızı belirler.
        TRIM_ARSPD_CM => Trim hava hızı (cm/s): İHA'nın trim hava hızını belirler, Trim hızı, İHA'nın belirli bir hızda istikrarlı bir şekilde uçmasını sağlar.
        """
move_road = """
            WPNAV_RADIUS => Yol noktası yarıçapı (m): İHA'nın bir yol noktasından ne kadar sapma yapabileceğini belirler, Bu parametre, İHA'nın daha 
                            doğru bir şekilde bir hedefe ulaşmasını sağlar. 
            RTL_ALT_FINAL => Dönüşteki son hedef yüksekliği (m): İHA'nın Geri Dönüş (RTL) modunda son hedefe ne kadar yükseklikte döneceğini belirler.
            RTL_ALT => Geri Dönüş yüksekliği (m): İHA'nın Geri Dönüş modunda varsayılan yüksekliği belirler.
            LAND_FLARE_ALT => İnişteki flare yüksekliği (m): İHA'nın iniş sırasında ne kadar yükseklikte flare yapacağını belirler, Flare, düşük hızlarda daha 
                                güvenli bir iniş sağlar.
            LOIT_RADIUS => Döngü yarıçapı (m): İHA'nın çevresinde döneceği bir noktanın yarıçapını belirler.
            LOIT_TYPE => Döngü tipi: İHA'nın çevresinde dönerken kullanılacak döngü tipini belirler.
            NAVL1_PERIOD => L1 denetleyici döngü süresi (s): İHA'nın rotasını daha iyi takip etmesini sağlar.
            WP_RADIUS => Yol noktası geçiş yarıçapı (m): İHA'nın bir yol noktasından geçerken ne kadar sapma yapabileceğini belirler, Bu, İHA'nın yol noktalarını 
                        daha hassas bir şekilde takip etmesini sağlar.
            """ 
            
fail_safe = """
            FS_GCS_ENABLE => Uzak bilgisayarla iletişim kesme: Uzak bilgisayarla iletişim kaybolduğunda İHA'nın nasıl tepki vereceğini belirler, Bu, iletişim kaybı 
                            durumunda İHA'nın otomatik olarak nasıl davranacağını kontrol eder.       
            THR_FAILSAFE => Gaz kesme güvenliği: İHA'nın gaz kesme durumunda nasıl tepki vereceğini belirler, Bu, İHA'nın güvenli bir şekilde durmasını sağlar.
            FS_GPS_ENABLE => GPS Failsafe Etkinleştirme: İHA'nın GPS sinyali kaybı durumunda uygulanacak failsafe stratejisini belirler.
            FS_BATT_ENABLE => Pil Failsafe Etkinleştirme: Pil gerilimi veya kapasite düşüşü durumunda uygulanacak failsafe stratejisini belirler.
            FS_THR_VALUE => Failsafe Gaz Kesme Değeri: Gaz kesme failsafe özelliği etkin olduğunda, İHA'nın uygulayacağı minimum gaz değerini belirler.
            FS_GCS_TIMEOUT => GCS Failsafe Zaman Aşımı: Yer istasyonu ile iletişim kaybı durumunda, İHA'nın ne kadar süre sonra failsafe stratejisini 
                            uygulayacağını belirler.
            FS_GPS_TIMEOUT => GPS Failsafe Zaman Aşımı: GPS sinyali kaybı durumunda, İHA'nın ne kadar süre sonra failsafe stratejisini uygulayacağını belirler.
            FS_BATT_VOLTAGE => Pil Gerilimi Failsafe Değeri: Pil gerilimi failsafe özelliği etkin olduğunda, İHA'nın uygulayacağı minimum pil gerilim değerini belirler.
            """
            
battery = """
            BATT_CAPACITY => Batarya kapasitesi (mAh): İHA'nın kullanılan batarya kapasitesini belirler, Bu, İHA'nın görev süresini etkileyen önemli bir parametredir.
            BATT_LOW_VOLT => Düşük batarya voltajı (V): Düşük batarya uyarısı için voltaj seviyesini belirler, Bu, İHA'nın batarya düzeyi düşük olduğunda bir uyarı 
                            vermesini sağlar.
            BATT_LOW_MAH => Düşük batarya kapasitesi (mAh): Düşük batarya uyarısı için kapasite seviyesini belirler, İHA'nın batarya kapasitesi düşük 
                            olduğunda bir uyarı verir.                
"""
kumanda = """
            RC_FEEL_RP => Uzaktan kumanda hissiyatı: Uzaktan kumanda tepkilerini düzenler, Bu parametre, pilotun İHA'ya verdiği komutlara nasıl bir tepki 
                            alacağını belirler.
            RC_SPEED => Uzaktan kumanda hızı: Uzaktan kumanda ile yapılan kontrol girişlerinin hızını belirler, Bu, pilotun İHA'yı nasıl kontrol edeceğini etkiler.

        """
memory = """
            LOG_BITMASK => Günlük maskesi: Günlüklemeyi etkinleştirmek veya devre dışı bırakmak için kullanılır, İHA'nın uçuş verilerini kaydetmesini kontrol eder.
        """

gps = """
        AHRS_GPS_GAIN => AHRS GPS kazancı: GPS tabanlı konumlandırma için kullanılan kazanç faktörünü belirler, Bu, İHA'nın daha doğru bir şekilde
                        konumlanmasını sağlar.
        COMPASS_OFS_X => Pusula ofseti X: Pusula ofsetlerini kalibre etmek için kullanılır, Bu parametre, İHA'nın pusulasının doğru bir şekilde çalışmasını sağlar.
        COMPASS_OFS_Y => Pusula ofseti Y: Pusula ofsetlerini kalibre etmek için kullanılır, Bu parametre, İHA'nın pusulasının doğru bir şekilde çalışmasını sağlar.
        COMPASS_OFS_Z => Pusula ofseti Z: Pusula ofsetlerini kalibre etmek için kullanılır, Bu parametre, İHA'nın pusulasının doğru bir şekilde çalışmasını sağlar.
        COMPASS_MOT_X => Pusula motor ofseti X: Motorlar çalıştığında pusula değerlerini düzeltmek için kullanılır, Motorların pusula okumalarını etkileyen 
                        manyetik alanları telafi eder.
        COMPASS_MOT_Y => Pusula motor ofseti Y: Motorlar çalıştığında pusula değerlerini düzeltmek için kullanılır, Motorların pusula okumalarını etkileyen 
                        manyetik alanları telafi eder.
        COMPASS_MOT_Z => Pusula motor ofseti Z: Motorlar çalıştığında pusula değerlerini düzeltmek için kullanılır, Motorların pusula okumalarını etkileyen 
                        manyetik alanları telafi eder.
        COMPASS_USE => Pusula kullanımı: Pusula kullanımını etkinleştirmek veya devre dışı bırakmak için kullanılır, İHA'nın pusula verilerini kullanıp 
                        kullanmayacağını kontrol eder.
"""
eksen = """
        AHRS_YAW_P - AHRS Yaw P terimi: Yaw (Yatay Eksen Eğimi) kontrol algoritmasının P terimi, Bu, İHA'nın yaw hareketini düzenler.
        AHRS_YAW_I - AHRS Yaw I terimi: Yaw kontrol algoritmasının I terimi, Bu, İHA'nın yaw hareketini düzenler.
        AHRS_YAW_D - AHRS Yaw D terimi: Yaw kontrol algoritmasının D terimi, Bu, İHA'nın yaw hareketini düzenler.
        AHRS_PITCH_P - AHRS Pitch P terimi: Pitch (Yatay Eksen Eğimi) kontrol algoritmasının P terimi, Bu, İHA'nın pitch hareketini düzenler.
        AHRS_PITCH_I - AHRS Pitch I terimi: Pitch kontrol algoritmasının I terimi, Bu, İHA'nın pitch hareketini düzenler.
        AHRS_PITCH_D - AHRS Pitch D terimi: Pitch kontrol algoritmasının D terimi, Bu, İHA'nın pitch hareketini düzenler.
        AHRS_ROLL_P - AHRS Roll P terimi: Roll (Dikey Eksen Eğimi) kontrol algoritmasının P terimi, Bu, İHA'nın roll hareketini düzenler.
        AHRS_ROLL_I - AHRS Roll I terimi: Roll kontrol algoritmasının I terimi, Bu, İHA'nın roll hareketini düzenler.
        AHRS_ROLL_D - AHRS Roll D terimi: Roll kontrol algoritmasının D terimi, Bu, İHA'nın roll hareketini düzenler.
        AHRS_TRIM_X - AHRS Trim X: İHA'nın trim düzeltmelerini X ekseni üzerinde belirler.
        AHRS_TRIM_Y - AHRS Trim Y: İHA'nın trim düzeltmelerini Y ekseni üzerinde belirler.
        AHRS_TRIM_Z - AHRS Trim Z: İHA'nın trim düzeltmelerini Z ekseni üzerinde belirler.
        AHRS_ORIENTATION - AHRS Yönelimi: İHA'nın yerleştirildiği konumu belirler, Bu, İHA'nın sensör verilerini doğru bir şekilde yorumlamasını sağlar.
        AHRS_GPS_GAIN - AHRS GPS kazancı: AHRS'nin GPS konum verilerini kullanma kazancını belirler, Bu, GPS verilerini daha hassas bir şekilde entegre eder.
        """
        
take_off = """
            THR_SLEWRATE - Gaz Değişim Hızı: İHA'nın gaz kontrolünün hızını belirler, Bu, İHA'nın hızlı gaz değişikliklerini daha yumuşak bir şekilde gerçekleştirmesini sağlar.
            THR_SLEWRATE_UP - Gaz Artırma Hızı: İHA'nın gazını artırma hızını belirler, Bu, İHA'nın hızlı bir şekilde yükselmesini sağlar.
            THR_SLEWRATE_DN - Gaz Azaltma Hızı: İHA'nın gazını azaltma hızını belirler, Bu, İHA'nın hızlı bir şekilde alçalmasını sağlar.
            TKOFF_THR_MINACC - Kalkış Minimum İvme: İHA'nın kalkış sırasında minimum ivmeye sahip olması gereken değeri belirler.
            TKOFF_THR_MAXACC - Kalkış Maksimum İvme: İHA'nın kalkış sırasında maksimum ivmeye sahip olması gereken değeri belirler. 
            TKOFF_THR_SLEW - Kalkış Gaz Değişim Hızı: İHA'nın kalkış sırasında gaz kontrolünü daha kontrollü bir şekilde gerçekleştirmesini sağlar.
            MIS_TAKEOFF_ALT - Otomatik Kalkış Yüksekliği: İHA'nın otomatik kalkış yapacağı hedef yüksekliği belirler.
            MIS_TAKEOFF_SPEED - Otomatik Kalkış Hızı: İHA'nın otomatik kalkış sırasında kullanacağı hızı belirler.
            MIS_TAKEOFF_THRUST - Otomatik Kalkış İtme Gücü: İHA'nın otomatik kalkış sırasında kullanacağı itme gücünü belirler.
            MIS_TAKEOFF_PITCH - Otomatik Kalkış Pitch Açısı: İHA'nın otomatik kalkış sırasında kullanacağı pitch açısını belirler.
"""