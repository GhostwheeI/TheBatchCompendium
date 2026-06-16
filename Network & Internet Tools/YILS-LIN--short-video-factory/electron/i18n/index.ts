import i18next from 'i18next'
import Backend from 'i18next-fs-backend'
import { app, BrowserWindow, ipcMain } from 'electron'
import { fileURLToPath } from 'node:url'
import path from 'node:path'
import { i18nCommonOptions } from './common-options'

const __dirname = path.dirname(fileURLToPath(import.meta.url))
process.env.APP_ROOT = path.join(__dirname, '..')

const localesPath = path.join(process.env.APP_ROOT, 'locales/{{lng}}/{{ns}}.json')

export const initI18n = async () => {
  await i18next.use(Backend).init({
    // initAsync: false,
    // debug: true,
    ...i18nCommonOptions,
    lng: app.getLocale(), // 获取系统语言
    backend: {
      loadPath: localesPath,
    },
  })

  // 获取多语言文件路径
  ipcMain.handle('i18n-getLocalesPath', () => localesPath)

  // 读取当前语言
  ipcMain.handle('i18n-getLanguage', () => i18next.language)

  // 渲染进程切换语言
  ipcMain.handle('i18n-changeLanguage', async (_, lng: string) => {
    await changeAppLanguage(lng)
    return lng
  })
}

export const changeAppLanguage = async (lng: string) => {
  await i18next.changeLanguage(lng)
  BrowserWindow.getAllWindows().forEach((win) => {
    win.webContents.send('i18n-changeLanguage', lng)
  })
}
