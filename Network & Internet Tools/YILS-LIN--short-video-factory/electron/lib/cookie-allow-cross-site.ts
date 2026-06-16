import { app, session } from 'electron'

/**
 * 解决 electron15 后，跨域cookie无法携带问题
 */
export default function useCookieAllowCrossSite() {
  app.whenReady().then(() => {
    const filter = { urls: ['https://*/*'] }
    session.defaultSession.webRequest.onHeadersReceived(filter, (details, callback) => {
      if (details.responseHeaders && details.responseHeaders['Set-Cookie']) {
        for (let i = 0; i < details.responseHeaders['Set-Cookie'].length; i++) {
          details.responseHeaders['Set-Cookie'][i] += ';SameSite=None;Secure'
        }
      }
      callback({ responseHeaders: details.responseHeaders })
    })
  })
}
