import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="منصة اختبارات العمران",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html_code = """
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>منصة اختبارات العمران</title>
    <style>
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #0b0f19;
            color: #f3f4f6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow-x: hidden;
        }

        #intro-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #000000;
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999;
            color: #ffffff;
            font-size: 1.8rem;
            text-align: center;
            padding: 20px;
            transition: opacity 0.5s ease;
        }

        .glass-crack {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 9998;
            display: none;
        }

        .glass-crack::before, .glass-crack::after {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: 
                radial-gradient(circle at 30% 40%, transparent 10%, rgba(255, 255, 255, 0.8) 10.5%, transparent 11%),
                radial-gradient(circle at 70% 60%, transparent 15%, rgba(255, 255, 255, 0.7) 15.5%, transparent 16%),
                linear-gradient(45deg, transparent 48%, rgba(255, 255, 255, 0.6) 49%, transparent 50%),
                linear-gradient(-45deg, transparent 48%, rgba(255, 255, 255, 0.6) 49%, transparent 50%),
                linear-gradient(20deg, transparent 60%, rgba(255, 255, 255, 0.5) 60.5%, transparent 61%),
                linear-gradient(75deg, transparent 30%, rgba(255, 255, 255, 0.5) 30.5%, transparent 31%);
        }

        #login-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: #0b0f19;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            z-index: 9990;
            padding: 20px;
        }

        .login-box {
            background: #111827;
            padding: 40px;
            border-radius: 12px;
            border: 1px solid #1f2937;
            text-align: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
            width: 100%;
            max-width: 400px;
        }

        .login-box input {
            width: 100%;
            padding: 12px;
            margin: 20px 0;
            background: #1f2937;
            border: 1px solid #374151;
            border-radius: 8px;
            color: #fff;
            font-size: 1rem;
            text-align: center;
        }

        .login-box button {
            background: #3b82f6;
            color: white;
            border: none;
            padding: 12px 25px;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            transition: background 0.3s;
            width: 100%;
        }

        .login-box button:hover {
            background: #2563eb;
        }

        .error-msg {
            color: #ef4444;
            margin-top: 10px;
            font-size: 0.9rem;
            display: none;
        }

        .main-container {
            flex: 1;
            display: none;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            padding: 40px 20px;
            text-align: center;
        }

        .menu-options {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;
            max-width: 400px;
        }

        .menu-box {
            background: #1f2937;
            border: 1px solid #374151;
            padding: 20px;
            border-radius: 10px;
            font-size: 1.2rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }

        .menu-box:hover {
            background: #374151;
            border-color: #4b5563;
            transform: translateY(-2px);
        }

        #subjects-screen {
            display: none;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 500px;
            margin: auto;
            padding: 20px;
        }

        .subject-box {
            background: #1f2937;
            border: 1px solid #374151;
            padding: 18px;
            margin: 10px 0;
            border-radius: 10px;
            width: 100%;
            text-align: center;
            font-size: 1.1rem;
            cursor: pointer;
            transition: all 0.3s;
        }

        .subject-box:hover {
            background: #374151;
        }

        #notes-screen {
            display: none;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            flex: 1;
            padding: 20px;
        }

        .notes-card {
            background: #1f2937;
            padding: 30px;
            border-radius: 12px;
            border: 1px solid #374151;
            text-align: center;
            max-width: 450px;
            width: 100%;
        }

        .notes-card h3 {
            margin-bottom: 15px;
            color: #60a5fa;
        }

        .notes-card p {
            font-size: 1.2rem;
            letter-spacing: 1px;
            color: #e5e7eb;
        }

        #quiz-screen {
            display: none;
            flex-direction: column;
            align-items: center;
            width: 100%;
            max-width: 700px;
            margin: auto;
            padding: 20px;
        }

        .question-card {
            background: #1f2937;
            border: 1px solid #374151;
            padding: 25px;
            border-radius: 12px;
            width: 100%;
            margin-bottom: 20px;
            text-align: right;
        }

        .question-card p {
            font-size: 1.1rem;
            margin-bottom: 15px;
            line-height: 1.6;
        }

        .question-card input {
            width: 100%;
            padding: 10px;
            background: #111827;
            border: 1px solid #4b5563;
            border-radius: 6px;
            color: #fff;
            margin-bottom: 10px;
        }

        .action-btn {
            background: #10b981;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.95rem;
            transition: background 0.3s;
        }

        .action-btn:hover {
            background: #059669;
        }

        .answer-reveal {
            margin-top: 10px;
            padding: 10px;
            background: #111827;
            border-radius: 6px;
            border-right: 4px solid #10b981;
            display: none;
            font-size: 0.95rem;
            color: #d1d5db;
        }

        .nav-level-btn {
            background: #3b82f6;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 8px;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 20px;
            transition: background 0.3s;
        }

        .nav-level-btn:hover {
            background: #2563eb;
        }

        .back-btn {
            background: #4b5563;
            color: white;
            border: none;
            padding: 8px 20px;
            border-radius: 6px;
            cursor: pointer;
            margin-bottom: 20px;
            align-self: flex-start;
        }

        .back-btn:hover {
            background: #374151;
        }

        footer {
            background: #030712;
            padding: 15px 20px;
            text-align: center;
            border-top: 1px solid #1f2937;
            font-size: 0.85rem;
            color: #9ca3af;
        }

        .footer-content {
            display: flex;
            flex-direction: column;
            gap: 8px;
            align-items: center;
            justify-content: center;
        }

        .verified-badge {
            display: inline-flex;
            align-items: center;
            gap: 4px;
            color: #60a5fa;
            font-weight: 500;
        }

        .verified-icon {
            width: 14px;
            height: 14px;
            background-color: #1d9bf0;
            border-radius: 50%;
            display: inline-flex;
            justify-content: center;
            align-items: center;
            color: white;
            font-size: 9px;
        }

        .stats-bar {
            display: flex;
            gap: 15px;
            justify-content: center;
            align-items: center;
            margin-top: 5px;
        }

        .encrypted-profit {
            background: #1f2937;
            padding: 2px 8px;
            border-radius: 4px;
            cursor: pointer;
            letter-spacing: 2px;
            color: #4b5563;
            user-select: none;
            transition: color 0.3s;
        }

        .profit-note {
            font-size: 0.8rem;
            color: #f87171;
            display: none;
            margin-top: 4px;
        }
    </style>
</head>
<body>

    <div id="intro-screen">
        يقال أن هذا الموقع لسكان الفئة واو الاصليين
    </div>

    <div class="glass-crack" id="glassCrack"></div>

    <div id="login-screen">
        <div class="login-box">
            <h3>تسجيل الدخول</h3>
            <input type="password" id="passwordInput" placeholder="أدخل كلمة المرور">
            <button onclick="checkPassword()">تسجيل الدخول</button>
            <div class="error-msg" id="errorMsg">كلمة المرور غير صحيحة</div>
        </div>
    </div>

    <div class="main-container" id="mainContainer">
        <div class="menu-options">
            <div class="menu-box" onclick="openSubjects()">اختبارات العمران</div>
            <div class="menu-box" onclick="openNotes()">اترك ملاحظاتك</div>
        </div>
    </div>

    <div id="subjects-screen">
        <button class="back-btn" onclick="goHome()">الرجوع للخلف</button>
        <div style="width: 100%; display: flex; flex-direction: column; gap: 15px;">
            <div class="subject-box" onclick="startQuiz('animal_care')">رعاية الحيوان</div>
            <div class="subject-box" onclick="alert('قريباً...')">أسس الإدارة والتلبية والمحاسبة</div>
            <div class="subject-box" onclick="alert('قريباً...')">أمراض النبات</div>
            <div class="subject-box" onclick="alert('قريباً...')">خصوبة التربة</div>
        </div>
    </div>

    <div id="notes-screen">
        <button class="back-btn" onclick="goHome()" style="margin-bottom: 20px;">الرجوع للخلف</button>
        <div class="notes-card">
            <h3>تواصل مع المصمم</h3>
            <p>0983957561</p>
        </div>
    </div>

    <div id="quiz-screen">
        <button class="back-btn" onclick="openSubjects()">الرجوع للمواد</button>
        <h2 id="quiz-title" style="margin-bottom: 20px; color: #60a5fa;"></h2>
        <div id="questions-container" style="width: 100%;"></div>
        <button class="nav-level-btn" id="nextLevelBtn" onclick="nextLevel()">التالي</button>
    </div>

    <footer>
        <div class="footer-content">
            <div>صمم من قبل المهندس أحمد علي عمران | جميع الحقوق محفوظة 2026©</div>
            <div class="verified-badge">
                تم التوثيق من قبل شركة USPT 
                <span class="verified-icon">✓</span>
            </div>
            <div class="stats-bar">
                <span>عدد المستخدمين: 1668</span>
                <span>|</span>
                <span>الأرباح: <span class="encrypted-profit" onclick="revealProfit()">••••••</span></span>
            </div>
            <div class="profit-note" id="profitNote">عذراً لا يمكن رؤية الأرباح الا من قبل المصمم®™</div>
        </div>
    </footer>

    <script>
        const animalCareLevels = [
            [
                { q: 'السؤال 1: ما المقصود بمصطلح "رعاية الحيوان الزراعي"؟', a: 'هي الإدارة العملية اليومية التي تمكن من تحقيق أهداف الإنتاج المستدام والتوازن بين المتطلبات الاقتصادية ومتطلبات الحيوان، بما يضمن توفير الشروط المثلى لإنتاج حيوانات المزرعة من حيث التغذية، المأوى، الرعاية الصحية، والبيئة المناسبة.' },
                { q: 'السؤال 2: ما هو الهدف الأساسي من منظومات رعاية الحيوان بحسب منظمة الصحة الحيوانية (WOAH)؟', a: 'تهدف إلى تحسين الصحة الجسدية والسلوكية للحيوانات، وتشمل الوقاية الفعّالة من الأمراض، والعلاج، وتسجيل الإصابات، وإدارة القطيع أو المجموعات الحيوانية بفعالية تحقق أعلى إنتاج بأقل قدر من الإجهاد والألم.' },
                { q: 'السؤال 3: ما هو الجوهر الأساسي لفلسفة حقوق الحيوان؟', a: 'يكمن في أن جميع الحيوانات تمتلك قدرة على الإحساس وتتمتع بقيمة أخلاقية مستقلة بغض النظر عن مدى فائدتها للبشر، ولها حقوق أساسية بما في ذلك الحق في الحياة.' },
                { q: 'السؤال 4: ماذا تعني قدرة الإحساس لدى الحيوان (Animal sentience)؟', a: 'تشير إلى قدرته على خوض تجارب ذاتية وتكوين أفكار ومشاعر مختلفة والتمتع بشخصيات فردية.' },
                { q: 'السؤال 5: ما الفرق الجوهري بين نهج "رفاهية الحيوان" ونهج "حقوق الحيوان"؟', a: 'رفاهية الحيوان تمثل نهجاً علمياً لتنظيم الممارسات لتقليل معاناة الحيوانات، بينما تستند فلسفة حقوق الحيوان إلى فكرة أنه لا ينبغي للبشر استخدام الحيوانات لأي سبب كان، وأن حقوق الحيوان يجب أن تحمي مصالحها تماماً مثل حقوق الإنسان.' },
                { q: 'السؤال 6: على كم أبعاد رئيسية تعتمد عملية تقييم رعاية الحيوان، وما هي؟', a: 'تعتمد على ثلاثة أبعاد رئيسية هي: السلوك، الفيزيولوجيا، والإدارة.' },
                { q: 'السؤال 7: كيف يتم استخدام البعد "السلوكي" كأداة في تقييم رعاية الحيوان؟', a: 'يعد وسيلة مباشرة لقراءة الحالة النفسية والعاطفية للحيوان؛ إذ يمكن الاستدلال على الراحة من خلال الاسترخاء والأنشطة الطبيعية، بينما تدل علامات مثل الحجلاء، ارتعاش الأذنين، أو حركة الذيل المضطربة على التوتر والخوف.' },
                { q: 'السؤال 8: ما هي المؤشرات الفيزيولوجية المستخدمة لقياس استجابة الحيوان للتوتر والرفاه؟', a: 'تُستخدم مؤشرات مثل قياس مستويات هرمون الكورتيزول والأدرينالين للاستجابة الفورية للتوتر، إضافة إلى مراقبة معدلات البرولاكتين والأوكسيتوسين لقياس التوازن الهرموني المرتبط بالحالة النفسية.' },
                { q: 'السؤال 9: ماذا تقيس "المقاييس القائمة على الحيوان" (Animal-Based Measures)؟', a: 'تقيس مباشرة على جسم وسلوك الحيوان لتوفير معلومات عن النتيجة الفعلية لظروف الرعاية، وتتضمن مؤشرات مثل حالة الجسم، وجود العرج، مستوى النظافة، وحالة الإصابات أو العلل الصحية.' },
                { q: 'السؤال 10: ماذا تقيس "المقاييس المعتمدة على نظام الإدارة" (Resource- and Management-Based Measures)؟', a: 'تقيس المؤشرات على البيئة المحيطة بالحيوان أو الموارد والإدارة المطبقة وتعد مؤشرات على المخاطر المحتملة.' },
                { q: 'السؤال 11: لماذا يُعد الجمع بين المقاييس القائمة على الحيوان وتلك المعتمدة على الإدارة هو المقياس المثالي؟', a: 'لأن المقياس القائم على الحيوان يخبرنا بوجود المشكلة أو تأثيرها على الحيوان، بينما يوضح المقياس القائم على نظام الإدارة سبب المشكلة، مما يتيح اتخاذ التدابير المناسبة لتحسين الرعاية.' },
                { q: 'السؤال 12: ما هما النموذجان البارزان المذكوران لقياس مدى نجاح أو إخفاق ممارسات رفاهية الحيوان؟', a: 'إطار الحريات الخمس ونموذج المجالات الخمسة.' },
                { q: 'السؤال 13: اذكر اثنتين من "الحريات الخمس" الأساسية لرفاهية الحيوان؟', a: 'التحرر من الجوع والعطش، والتحرر من الألم والإصابة والمرض.' },
                { q: 'السؤال 14: ما الذي يميز "نموذج المجالات الخمسة" عن مفهوم "الحريات الخمس"؟', a: 'إنه نموذج أكثر شمولاً؛ إذ يتعمق في دراسة الحالة الذهنية للحيوان، ويركز على التجارب الإيجابية والعوامل المسببة لها بدلاً من الاكتفاء بالتركيز على منع التجارب السلبية فقط.' },
                { q: 'السؤال 15: كيف تختلف حالة الدجاجة البياضة التي تعيش في نظام التربية الطلق عنها في نظام الأقفاص العمودية؟', a: 'الدجاجة في التربية الطلق تتمتع بحرية الاستكشاف وممارسة السلوكيات الطبيعية وحالة نفسية إيجابية، بينما تعاني المحتجزة في البطاريات من الاكتظاظ ومساحة ضئيلة وانعدام القدرة على الحركة.' }
            ],
            [
                { q: 'السؤال 1: لماذا يُعد فهم سلوك الخيول أمراً مهمّاً في مجالات التربية والتدريب؟', a: 'لانه يضمن التعامل الآمن والفعال معها، ويساعد المربين على تحسين أساليب التربية وتعزيز قدرات الخيول وتقليل مخاطر الحوادث.' },
                { q: 'السؤال 2: ما هما النمطان الأساسيان للسلوك عند الخيول؟', a: 'السلوك الفطري والسلوك المكتسب.' },
                { q: 'السؤال 3: ما هو المقصود بـ "سلوك الهروب" عند الخيول؟', a: 'هو امتلاك الخيول غريزة قوية للهروب من التهديدات عندما تشعر بالخوف أو الضغط.' },
                { q: 'السؤال 4: ما هي أهم الأسباب التي تؤدي إلى ظهور "سلوك النساج" (Weaving)؟', a: 'الملل والافتقار إلى التحفيز، التوتر والقلق، الحرمان الاجتماعي، والتوقع الزائد لحدوث نشاط معين.' },
                { q: 'السؤال 5: اذكر بعض مظاهر "سلوك الشر" (العدوانية) عند الخيول.', a: 'العض، الركل أو الترفس، الرفس أو النطح، والتحرك العدواني بسرعة.' },
                { q: 'السؤال 6: ما هي أبرز الأسباب التي تؤدي إلى حدوث "سلوك أكل الروث" (Coprophagia)؟', a: 'نقص العناصر الغذائية، الملل أو الضجر، الفضول عند الأمهار الصغيرة، وسوء إدارة التغذية.' },
                { q: 'السؤال 7: ما هي المخاطر الصحية الناتجة عن "سلوك أكل الروث"؟', a: 'خطر الإصابة بالطفيليات والأمراض واضطرابات الجهاز الهضمي.' },
                { q: 'السؤال 8: ما هو "سلوك اللسان المتدلي" وكيف يمكن أن تساهم الأضرار الجسدية في حدوثه؟', a: 'هو إخراج الحصان لسانه خارج فمه؛ وتساهم الأضرار الجسدية مثل تقرحات الفم أو الأسنان الحادة في ذلك لتخفيف الألم.' },
                { q: 'السؤال 9: كيف يؤدي "التعرض لظروف مختلفة" إلى تطوير السلوك المكتسب الإيجابي؟', a: 'من خلال التعرض المتكرر بشكل مدروس لمواقف مختلفة مما يساهم في تعلم كيفية التحكم في الخوف وزيادة الثقة.' },
                { q: 'السؤال 10: ما هو المقصود بـ "سلوك بلع الهواء" (Cribbing)؟', a: 'وضع الأسنان على سطح صلب وسحب الهواء إلى داخل المريء مع إصدار صوت مميز.' },
                { q: 'السؤال 11: ما هي الأسباب الرئيسية لحدوث "سلوك التجول المفرط" (Box Walking)؟', a: 'الملل، التوتر والقلق، الفصل الاجتماعي، ونقص التمرين.' },
                { q: 'السؤال 12: كيف يمكن التعامل مع سلوك "رفض العمل" (Bulking) باستخدام التدريب الإيجابي؟', a: 'من خلال استخدام أساليب التدريب الإيجابية والمكافآت والثناء عند الاستجابة للأوامر.' },
                { q: 'السؤال 13: ماذا يقصد بـ "سلوك القطيع" عند الخيول؟', a: 'عيش الخيول في مجموعات حيث يعتمد كل منها على الآخر في الحماية وفضل البقاء بالقرب من القطيع.' },
                { q: 'السؤال 14: كيف يمكن علاج أو التعامل مع "سلوك بلع الهواء" من الناحية الغذائية؟', a: 'عن طريق زيادة تقديم الألياف مثل التبن لمساعدة الحصان في الشعور بالشبع وتحفيز الجهاز الهضمي.' },
                { q: 'السؤال 15: لماذا تلجأ الخيول إلى "سلوك البحث عن الطعام" في البيئة الطبيعية؟', a: 'لانها تميل إلى البحث عن الطعام بشكل مستمر حيث تقضي وقتاً طويلاً في الرعي.' }
            ],
            [
                { q: 'السؤال 1: ما هو تعريف سلوك التجول المفرط (Box Walking) عند الخيول؟', a: 'سلوك غير طبيعي حيث تتحرك الخيول بشكل مستمر في دوائر أو من جانب لآخر داخل إسبلها بسبب الملل أو التوتر.' },
                { q: 'السؤال 2: ما أبرز أسباب ظهور سلوك التجول المفرط لدى الخيول؟', a: 'الملل، التوتر والقلق، الفصل الاجتماعي، ونقص التمرين.' },
                { q: 'السؤال 3: كيف يمكن التعامل مع مشكلة التجول المفرط عبر تحسين البيئة؟', a: 'عبر تحسين الإسبل بإضافة إضاءة جيدة، تهوية مناسبة، وتقديم نظام غذائي متوازن يحتوي على الألياف.' },
                { q: 'السؤال 4: ماذا يُقصد بسلوك "رفض العمل" (Balking) عند الخيول؟', a: 'سلوك يظهره الحصان عندما يتردد أو يرفض تنفيذ أمر ما كالمشي أو الجري أو القفز.' },
                { q: 'السؤال 5: ما هي أبرز الأسباب التي تؤدي إلى رفض الحصان للعمل؟', a: 'الخوف، الألم، عدم الثقة، التعب، والتحفيز غير الكافي.' },
                { q: 'السؤال 6: ما هو العنصر الحاسم في نجاح أي نظام لإيواء الأرانب على المدى الطويل؟', a: 'الالتزام بالمعايير الفنية السليمة وتطبيق مبادئ الإدارة الرشيدة.' },
                { q: 'السؤال 7: اذكر اثنين من الاعتبارات الأساسية في تصميم مساكن الأرانب.', a: 'التهوية لضمان تيار هواء متجدد، والحماية من الظروف الجوية القاسية والمفترسات.' },
                { q: 'السؤال 8: ما هو النظام الأكثر شيوعاً في التربية المكثفة للأرانب وما أبرز عيوبه؟', a: 'نظام الأقفاص، ومن عيوبه التكاليف الإنشائية المرتفعة ومحدودية الحركة.' },
                { q: 'السؤال 9: ما الفائدة من استخدام نظام الأكوام (Hutch System) في تربية الأرانب؟', a: 'مثالي لتربية عدد قليل من الأرانب منزلياً بتكلفة منخفضة وملجأ آمن.' },
                { q: 'السؤال 10: ما هما المكونان الأساسيان اللذان يُميزان عملية الهضم عند الأرانب؟', a: 'الاقترات الكاذب والتخمير الميكروبي في الأعور.' },
                { q: 'السؤال 11: ما هي أهم المكونات الرئيسية التي يجب أن تحتوي عليها علائق الأرانب المتزنة؟', a: 'المركزات، الأعلاف الخشنة، والأعلاف الخضراء.' },
                { q: 'السؤال 12: ما المقصود بمؤشر "التحويل الغذائي" لدى الأرانب؟', a: 'كمية العلف اللازمة لإنتاج كيلو جرام واحد من اللحم وتتراوح بين 3:1 إلى 4:1.' },
                { q: 'السؤال 13: ما هي أبرز المشاكل الشائعة المرتبطة بالتغذية لدى الأرانب؟', a: 'الإسهال، انتفاخ المعدة والأمعاء، والكوسيديا.' },
                { q: 'السؤال 14: كم تستغرق دورة الإنتاج الأساسية لأنثى الأرنب في المتوسط؟', a: 'بين 42 إلى 49 يوماً تتوزع بين الحمل والرضاعة.' },
                { q: 'السؤال 15: ما هي أهم العوامل المؤثرة على طول وكفاءة الحياة الإنتاجية للأرانب؟', a: 'الوراثة، التغذية، الإدارة والرعاية، كثافة الإنتاج، والصحة.' }
            ]
        ];

        let currentLevelIndex = 0;

        window.addEventListener('DOMContentLoaded', () => {
            setTimeout(() => {
                document.getElementById('intro-screen').style.opacity = '0';
                setTimeout(() => {
                    document.getElementById('intro-screen').style.display = 'none';
                    document.getElementById('glassCrack').style.display = 'block';
                    setTimeout(() => {
                        document.getElementById('glassCrack').style.display = 'none';
                        document.getElementById('login-screen').style.display = 'flex';
                    }, 1500);
                }, 500);
            }, 7000);
        });

        function checkPassword() {
            const pass = document.getElementById('passwordInput').value;
            if (pass === 'ركوب أعلى موجة') {
                document.getElementById('login-screen').style.display = 'none';
                document.getElementById('mainContainer').style.display = 'flex';
            } else {
                document.getElementById('errorMsg').style.display = 'block';
            }
        }

        function openSubjects() {
            document.getElementById('mainContainer').style.display = 'none';
            document.getElementById('quiz-screen').style.display = 'none';
            document.getElementById('subjects-screen').style.display = 'flex';
        }

        function openNotes() {
            document.getElementById('mainContainer').style.display = 'none';
            document.getElementById('notes-screen').style.display = 'flex';
        }

        function goHome() {
            document.getElementById('subjects-screen').style.display = 'none';
            document.getElementById('notes-screen').style.display = 'none';
            document.getElementById('mainContainer').style.display = 'flex';
        }

        function startQuiz(subject) {
            if (subject === 'animal_care') {
                currentLevelIndex = 0;
                document.getElementById('subjects-screen').style.display = 'none';
                document.getElementById('quiz-screen').style.display = 'flex';
                loadLevel(currentLevelIndex);
            }
        }

        function loadLevel(levelIdx) {
            document.getElementById('quiz-title').innerText = `رعاية الحيوان - المستوى ${levelIdx + 1}`;
            const container = document.getElementById('questions-container');
            container.innerHTML = '';

            animalCareLevels[levelIdx].forEach((item, index) => {
                const card = document.createElement('div');
                card.className = 'question-card';
                card.innerHTML = `
                    <p>${item.q}</p>
                    <input type="text" id="q_${index}" placeholder="اكتب الجواب هنا...">
                    <button class="action-btn" onclick="checkAnswer(${index}, \`${item.a.replace(/"/g, '&quot;')}\`)">انتهيت</button>
                    <div class="answer-reveal" id="ans_${index}"><strong>الجواب الصحيح:</strong> ${item.a}</div>
                `;
                container.appendChild(card);
            });

            const nextBtn = document.getElementById('nextLevelBtn');
            if (levelIdx < animalCareLevels.length - 1) {
                nextBtn.innerText = 'التالي';
                nextBtn.style.display = 'block';
            } else {
                nextBtn.innerText = 'إنهاء الاختبار وتقييم الدراسة';
                nextBtn.style.display = 'block';
            }
        }

        function checkAnswer(index, correctAns) {
            const ansDiv = document.getElementById(`ans_${index}`);
            ansDiv.style.display = 'block';
        }

        function nextLevel() {
            currentLevelIndex++;
            if (currentLevelIndex < animalCareLevels.length) {
                loadLevel(currentLevelIndex);
                window.scrollTo({ top: 0, behavior: 'smooth' });
            } else {
                const container = document.getElementById('questions-container');
                document.getElementById('quiz-title').innerText = 'نتيجة التقييم النهائي';
                container.innerHTML = `
                    <div style="background: #1f2937; padding: 40px; border-radius: 12px; text-align: center;">
                        <h3 style="color: #10b981; font-size: 1.8rem; margin-bottom: 15px;">تهانينا لك!</h3>
                        <p style="font-size: 1.2rem; margin-bottom: 10px;">تم إتمام جميع مستويات اختبارات رعاية الحيوان بنجاح.</p>
                        <p style="font-size: 1.5rem; color: #60a5fa; font-weight: bold;">تقييم دراستك: 100%</p>
                    </div>
                `;
                document.getElementById('nextLevelBtn').style.display = 'none';
            }
        }

        function revealProfit() {
            const note = document.getElementById('profitNote');
            note.style.display = note.style.display === 'block' ? 'none' : 'block';
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=900, scrolling=True)
