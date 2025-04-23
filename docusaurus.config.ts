import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'জানার ইচ্ছা জিঙ্গাসা',
  tagline: '',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://nemo97.github.io',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'nemo97', // Usually your GitHub org/user name.
  projectName: 'jij', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/nemo97/jij_docs/tree/main/docs',
        },
        blog: {
          showReadingTime: true,
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/nemo97/jij_docs/tree/main/docs',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],
  plugins: [
    'plugin-image-zoom'
  ],
  themeConfig: {
      imageZoom: {
            // CSS selector to apply the plugin to, defaults to '.markdown img'
            selector: '.markdown img',
            // Optional medium-zoom options
            // see: https://www.npmjs.com/package/medium-zoom#options
          },
    // Replace with your project's social card
    image: 'img/social-card.svg',
    navbar: {
      title: 'JIJ',
      logo: {
        alt: 'JIJ Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          to: '/docs/intro',
          activeBasePath: 'docs',         
          position: 'left',
          label: 'Getting Started',
        },
        {
          to: '/docs/primary/intro',          
          position: 'left',
          label: 'Primary',
        },
     /*   {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar2',
          position: 'left',
          label: 'Primary Student',
        },
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar3',
          position: 'left',
          label: 'Secondary Student',
        },
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar3',
          position: 'left',
          label: 'HS Student',
        },
        {
          type: 'docSidebar',
          sidebarId: 'tutorialSidebar4',
          position: 'left',
          label: 'HS+ Student',
        }, */
        {
          href: 'https://github.com/nemo97/jij_docs',
          position: 'right',
          className: 'header-github-link',
          'aria-label': 'GitHub repository',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
          ],
        }
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.jettwaveDark,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
