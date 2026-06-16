import { InitOptions } from 'i18next'

export const i18nLanguages = [
  { code: 'en', name: 'English' },
  { code: 'zh-CN', name: '简体中文' },
]

export const i18nCommonOptions: InitOptions = {
  fallbackLng: i18nLanguages[0].code,
  supportedLngs: i18nLanguages.map((l) => l.code),
  load: 'currentOnly',
  ns: ['common'],
  defaultNS: 'common',
  interpolation: { escapeValue: false },
}
