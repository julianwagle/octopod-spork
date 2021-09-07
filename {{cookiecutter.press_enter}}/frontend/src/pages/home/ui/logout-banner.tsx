import { AuthCosumer } from 'router';
import { Banner as UIBanner, Container } from 'ui';
import { APP_NAME } from 'config';

export const LogoutBanner: React.FC = () => (
  <AuthCosumer>
    {({ isAuth }) =>
      isAuth ? null : (
        <UIBanner>
          <Container>
            <h1 className="logo-font">{APP_NAME.toLowerCase()}</h1>
            <p>The front end of your new app.</p>
          </Container>
        </UIBanner>
      )
    }
  </AuthCosumer>
);
