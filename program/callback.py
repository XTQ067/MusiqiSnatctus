

from driver.queues import QUEUE
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardButton, InlineKeyboardMarkup
from config import (
    ASSISTANT_NAME,
    BOT_NAME,
    BOT_USERNAME,
    GROUP_SUPPORT,
    OWNER_NAME,
    UPDATES_CHANNEL,
)


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Xoş Gəldin [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**\n
💭 **[{BOT_NAME}](https://t.TrendMusiqiBot) allows you to play music and video on groups through the new Telegram's video chats!**

💡 **Üzərinə toxun və botun bütün əmrlərini və necə işlədiyini öyrənin😜 » 📚 Commands button!**

🔖 **Bu botdan necə istifadə edəcəyini bilmək üçün üzərinə toxunun🫂 » ❓ Basic Guide button!**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ Qrupa əlavə et ➕",
                        url=f"https://t.me/TrendMusiqiBot?startgroup=true",
                    )
                ],
                [InlineKeyboardButton("❓ Basic Guide", callback_data="cbhowtouse")],
                [
                    InlineKeyboardButton("📚 Commands", callback_data="cbcmds"),
                    InlineKeyboardButton("❤ Sahibim", url=f"https://t.me/ismayilzade075"),
                ],
                [
                    InlineKeyboardButton(
                        "👥 Official Support Qrup", url=f"https://t.me/TrendSupportGroup"
                    ),
                    InlineKeyboardButton(
                        "📣 Official Support Kanal", url=f"https://t.me/TrendProject"
                    ),
                ],
                [
                    InlineKeyboardButton(
                        "Help", url="https://t.me/ismayilzade075"
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""❓ **Basic Guide for using this bot:**

1.) **Əvvəlcə, mənı öz qrupuna əlavə et.**
2.) **Sonra mənı admin yetkisi verin.**
3.) **Daha Sonra adminləri yeniləmək üçün /reload əmrini verin.**
3.) **Qrupunuza @LuksMusicAsistant əlavə edin və ya onu dəvət etmək üçün /userbotjoin yazın.**
4.) **Video/musiqi oynatmağa başlamazdan əvvəl ilk olaraq video çatı yandırın.**
5.) **Bəzən /reload əmrindən istifadə edərək botun yenidən yüklənməsi bəzi problemi həll etməyə kömək edə bilər.**

📌 **İstifadəçi robotu video çata qoşulmayıbsa, video çatın artıq aktiv olub olmadığına əmin olun və ya /userbotleave yazın, sonra yenidən /userbotjoin yazın.**

💡 **Bu botla bağlı əlavə suallarınız varsa, onu buradakı dəstək çatımda deyə bilərsiniz: @TrendSupportGroup**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""✨ **Salam [{query.message.chat.first_name}](tg://user?id={query.message.chat.id}) !**

» **izahatı oxumaq və mövcud əmrlərin siyahısına baxmaq üçün aşağıdakı düyməni basın!**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("👷🏻 Admin Cmd", callback_data="cbadmin"),
                    InlineKeyboardButton("🧙🏻 Sudo Cmd", callback_data="cbsudo"),
                ],[
                    InlineKeyboardButton("📚 Basic Cmd", callback_data="cbbasic")
                ],[
                    InlineKeyboardButton("🔙 Go Back", callback_data="cbstart")
                ],
            ]
        ),
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the basic commands:

» /mplay (song name/link) - səsli söhbətdə musiqi çalın
» /stream (query/link) - yt canlı/radio canlı musiqini yayımlayın
» /vplay (video name/link) - səsli söhbəttə video oynatın 
» /vstream - yt live/m3u8-dən canlı video oynayın
» /playlist - sizə playlisti göstərər
» /video (query) - YouTube'dan video endir
» /song (query) - YouTube'dan musiqi endir
» /lyric (query) - Musiqi sözlərini tapar
» /search (query) - YouTube video linkini axtarın

» /ping - botun ping vəziyyəti
» /uptime - Botun işləmə müddətini göstərər
» /alive - botun canlı məlumatını göstərin (qrupda)

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the admin commands:

» /pause - botu dayandırar
» /resume - botu davam etdirər
» /skip - növbəti video/Musiqiyə keçər
» /stop - Bot oxumağı bitirər
» /vmute - səsli söhbətdə istifadəçi robotunun səsini söndürün
» /vunmute - Səsli söhbəttə İstifadəçi botun səsini açın 
» /volume `1-200` - botun səsini artırın (sadəcə adminlər)
» /reload - admin listini yeniləyin
» /userbotjoin - userbot qrupa qatılar
» /userbotleave - userbot qrupdan ayrılar

⚡️ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )

@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""🏮 here is the sudo commands:

» /rmw - bütün xam faylları təmizləyin
» /rmd - bütün yüklənmiş faylları təmizləyin
» /sysinfo - sistem məlumatlarını göstərin
» /update - botunuzu ən son versiyaya yeniləyin
» /restart - botu yeniləyin
» /leaveall - userbotun bütün qrupdan çıxmasını əmr edin

⚡ __Powered by {BOT_NAME} AI__""",
        reply_markup=InlineKeyboardMarkup(
            [[InlineKeyboardButton("🔙 Go Back", callback_data="cbcmds")]]
        ),
    )


@Client.on_callback_query(filters.regex("cbmenu"))
async def cbmenu(_, query: CallbackQuery):
    if query.message.sender_chat:
        return await query.answer("you're an Anonymous Admin !\n\n» revert back to user account from admin rights.")
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 only admin with manage voice chats permission that can tap this button !", show_alert=True)
    chat_id = query.message.chat.id
    if chat_id in QUEUE:
          await query.edit_message_text(
              f"⚙️ **settings of** {query.message.chat.title}\n\n⏸ : pause stream\n▶️ : resume stream\n🔇 : mute userbot\n🔊 : unmute userbot\n⏹ : stop stream",
              reply_markup=InlineKeyboardMarkup(
                  [[
                      InlineKeyboardButton("⏹", callback_data="cbstop"),
                      InlineKeyboardButton("⏸", callback_data="cbpause"),
                      InlineKeyboardButton("▶️", callback_data="cbresume"),
                  ],[
                      InlineKeyboardButton("🔇", callback_data="cbmute"),
                      InlineKeyboardButton("🔊", callback_data="cbunmute"),
                  ],[
                      InlineKeyboardButton("🗑 Close", callback_data="cls")],
                  ]
             ),
         )
    else:
        await query.answer("❌ hazırda heç nə yayımlanmır", show_alert=True)


@Client.on_callback_query(filters.regex("cls"))
async def close(_, query: CallbackQuery):
    a = await _.get_chat_member(query.message.chat.id, query.from_user.id)
    if not a.can_manage_voice_chats:
        return await query.answer("💡 yalnız səsli söhbətləri idarə etmək icazəsi olan admin bu düyməyə toxuna bilər!", show_alert=True)
    await query.message.delete()
