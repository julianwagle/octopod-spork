import { createBrowserHistory } from 'history';

export type { Location } from 'history';

export const history = createBrowserHistory({
  basename: '/app',
});
