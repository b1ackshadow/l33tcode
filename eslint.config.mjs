import pluginJs from "@eslint/js";
import tseslint from "typescript-eslint";


export default [
  { files: ["**/*.{js,mjs,cjs,ts}"] },
  pluginJs.configs.recommended,
  ...tseslint.configs.recommended,
  {
    rules: {
      semi: "error",
      "prefer-const": "error"
    }
  },
  {
    rules: {
      "@typescript-eslint/no-unsafe-call": 0
    }
  }
];
