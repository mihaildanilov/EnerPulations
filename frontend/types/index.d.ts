export type SiteConfig = {
  name: string;
  description: string;
};

export type Settings = {
  themeToggleEnabled: boolean;
};

export type Layout = {
  heroHeader: string;
  featureCards: string;
  headers: {
    featureCards: string;
    features: string;
  };
};
