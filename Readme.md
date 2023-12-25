Simple store
This is General Store and Sell general items
1. Check Inventory
2. Buy
3. Sell
4. Talk
0. Exit

Main python
. main.py
    program စ run ရင် main.py ကနေစ run ပါ။

Modules
. player_stats
    player_stats သည် player ရဲ့ ပိုက်ဆံ၊ အိတ်၊ စတာတွေကို စုစည်းထားသည်။
. function_module
    function_module သည် အပေါ်က list ထဲက အကြောင်းအရာတွေကို ထပ်မံစီစစ်ဖို့။
. Buy_and_Sell
    Buy_and_Sell သည် အရောင်းအဝယ်သီသန့် module ဖြစ်သည်။
. Storage_room
    Storage_room သည် ဆိုင်ကရောင်းမဲ့ ပစ္စည်းတွေကို စျေးနှုန်းနဲ့တကွသိမ်းဆည်းထားသည်။
. Show_consoles
    Player_inventory and Shop_items တွေကို console platform ကနေသပ်သပ်ရပ်ရပ်ဖြစ်အောင်ပြသည်။
. takling_module
    ဆိုင်ရှင်နဲ့ စကားအပြန်အလှန်ပြောဆိုရင်း ရင်းနှီးမှုရရှိအောင်လုပ်သည်။

Other files
. code_doodle.py
    သင်္ချာတွက်တဲ့အခါ အကြမ်းစာရွက်မှာ ချတွက်ကြည့်သလိုမျိုး code_doodle မှာလည်းချရေးကြည့်တယ်။
. Temp_code.md
    အကြမ်းတွက်ကြည့်လို့ ထွက်လာတဲ့ အချောကို Temp_code.md စာဖိုင်မှာ save တယ်။ လိုအပ်ရင် ပြန်ယူသုံးတယ်။

Daily Reports
Day 1 --> အခြေခံ Sturcture တည်ဆောက်ပြီးပြီ။ Function ထဲမှာလည်း Check Inventory ကို ရေးဆွဲပြီးပြီ။ Buy ကိုတော့နောက်နေ့မှပဲ ဆက်ရေးတော့မယ်။ 

Day 2 --> Buy() ကိစ္စပြီးပြီ၊ ဒါပေမဲ့ တော်တော်သိရှိလိုက်ရတယ်။ Global var ကို Function ထဲမှာအပြောင်းအလည်းလုပ်ချင်ရင် Function ထဲမှာ ကိုယ်ပြောင်းချင်တဲ့ Global var ကို global Global var ဆိုပြီးကြေညာပေးရတယ်။ မနက်ဖြန် Sell() ထပ်သွားမယ်။

Day 3 --> ဒီနေ့တော့ sell() ကိုမသွားနိုင်ခဲ့ဘူး buy() ကို ပြုပြင် ပြင်ဆင်ရင်းနဲ့ အချိန်ကုန်သွားတယ်။
player_stats module ထဲက variable ကို တခြားmodule ထဲကနေရိုးရိုးပုံစံနဲ့ လှမ်းပြောင်းလို့မရဘူး။ memmory address , memmory system တွေနဲ့ဆိုင်မယ်ထင်တယ်။ ဒါ့ကြောင့် player_stats ထဲမှာ variable အစား list data type ကိုသုံးလိုက်တယ်။ အဲဒါမှာ တခြားmodule ထဲကနေပြောင်းမှ player_stats ထဲမှာပါလိုက်ပြောင်းတာ။

Day 4 --> ဒီနေ့ sell() ပြီးသွားပြီ။ လိုအပ်တဲ့ပြင်ဆင်မှုတွေ၊ အမြင်ရှင်းအောင်ချိန်ညှိ ပြီးပြီ။ random module ကို သုံးပြီး sell percent ကို ထိန်းညှိတာတွေ Storage_room, Show_consoles ဆိုပြီး module အသစ်တည်ဆောက်တာတွေလုပ်ပြီးပြီ။

Day 5 --> ဒီနေ့ အကုန်ပြီးပြီ၊ ပြုပြင်မွမ်းမံဖို့ပဲလိုတော့တယ်။ အရင်ရေးထားတဲ့ buy() ထဲမှာ အသစ်နေနဲ့ loop_capacity တိုးတဲ့ program ပါရေးထားတယ်။ player_inventory က capacity နည်းလို့ အစ္စည်းတွေအများကြီးထည့်လို့မရဘူး။ ဒါ့ကြောင့် loop_capacity တိုးချင်ရင် အိတ်အသစ်ဝယ်ပြီး၊ capacity တိုး။ capacity တိုးတဲ့အခါမှာလည်းရှိပြီးသား capacity ပေါ်မှုတည်ပြီး ဝယ်လို့ရတာမရတာပါ သတ်မှတ်ထားတယ်။ အကယ်၍ ကိုယ်ဝယ်မဲ့ capacity size က ရှိပြီးသား သို့မဟုတ် ကိုယ့်ဟာထက် သေးနေရင် ဝယ်လို့မရပါဘူး။

# Creator --> Swam Htet Hein (ExTUS)