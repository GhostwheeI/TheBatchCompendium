import { categories } from '../../data/categories';
import { configCategories } from '../../data/categories';

const CategoryNavigation = () => {
  const scrollToSection = (id) => {
    const element = document.getElementById(`category-${id}`);
    if (element) {
      const offset = 180; // Account for sticky header and action bar
      const elementPosition = element.getBoundingClientRect().top;
      const offsetPosition = elementPosition + window.pageYOffset - offset;

      window.scrollTo({
        top: offsetPosition,
        behavior: 'smooth'
      });
    }
  };

  const allCategories = [
    ...categories.sort((a, b) => a.order - b.order),
    ...configCategories.map(cat => ({ ...cat, isConfig: true }))
  ];

  return (
    <div className="win98-raised" style={{ padding: '4px', marginBottom: '8px' }}>
      <div style={{ display: 'flex', flexDirection: 'column', gap: '2px' }}>
        {allCategories.map((category) => (
          <button
            key={category.id}
            onClick={() => scrollToSection(category.id)}
            className="win98-button"
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: '6px',
              width: '100%',
              justifyContent: 'flex-start',
              padding: '4px 8px',
              fontSize: '11px',
              textAlign: 'left'
            }}
            title={category.name}
          >
            <span style={{ fontSize: '14px', flexShrink: 0 }}>{category.icon}</span>
            <span>{category.name}</span>
          </button>
        ))}
      </div>
    </div>
  );
};

export default CategoryNavigation;
